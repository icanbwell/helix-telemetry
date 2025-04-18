from typing import Optional, Union, Mapping

from opentelemetry.context import Context
from opentelemetry.metrics import UpDownCounter

from helixtelemetry.telemetry.structures.telemetry_attribute_value import (
    TelemetryAttributeValue,
    TelemetryAttributeValueWithoutNone,
)
from helixtelemetry.telemetry.structures.telemetry_parent import TelemetryParent
from helixtelemetry.telemetry.utilities.mapping_appender import append_mappings


class TelemetryUpDownCounter:
    """
    This class wraps the OpenTelemetry UpDownCounter class and adds the supplied attributes every time a metric is recorded

    """

    def __init__(
        self,
        *,
        counter: UpDownCounter,
        attributes: Optional[Mapping[str, TelemetryAttributeValue]],
        telemetry_parent: Optional[TelemetryParent],
    ) -> None:
        assert counter
        self._counter: UpDownCounter = counter
        self._attributes: Optional[Mapping[str, TelemetryAttributeValue]] = attributes
        self._telemetry_parent: Optional[TelemetryParent] = telemetry_parent

    def add(
        self,
        amount: Union[int, float],
        attributes: Optional[Mapping[str, TelemetryAttributeValue]] = None,
        context: Optional[Context] = None,
    ) -> None:

        combined_attributes: Mapping[str, TelemetryAttributeValueWithoutNone] = (
            append_mappings(
                [
                    self._attributes,
                    self._telemetry_parent.attributes if self._telemetry_parent else {},
                    attributes,
                ]
            )
        )

        self._counter.add(
            amount=amount, attributes=combined_attributes, context=context
        )
