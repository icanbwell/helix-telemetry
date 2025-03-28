from typing import Any, Dict, Optional

from helixtelemetry.telemetry.providers.console_telemetry import ConsoleTelemetry
from helixtelemetry.telemetry.providers.null_telemetry import NullTelemetry
from helixtelemetry.telemetry.providers.open_telemetry import OpenTelemetry
from helixtelemetry.telemetry.providers.telemetry import Telemetry
from helixtelemetry.telemetry.spans.telemetry_span_creator import TelemetrySpanCreator
from helixtelemetry.telemetry.structures.telemetry_parent import TelemetryParent
from helixtelemetry.telemetry.structures.telemetry_provider import TelemetryProvider


class TelemetryFactory:
    def __init__(self, *, telemetry_parent: TelemetryParent) -> None:
        """
        Telemetry factory used to create telemetry instances based on the telemetry context


        :param telemetry_parent: telemetry parent
        """
        self.telemetry_parent = telemetry_parent

    def create(self, *, log_level: Optional[str | int]) -> Telemetry:
        """
        Create a telemetry instance

        :return: telemetry instance
        """
        if not self.telemetry_parent.telemetry_context:
            return NullTelemetry(
                telemetry_context=self.telemetry_parent.telemetry_context
            )

        match self.telemetry_parent.telemetry_context.provider:
            case TelemetryProvider.CONSOLE:
                return ConsoleTelemetry(
                    telemetry_context=self.telemetry_parent.telemetry_context,
                    log_level=log_level,
                )
            case TelemetryProvider.OPEN_TELEMETRY:
                return OpenTelemetry(
                    telemetry_context=self.telemetry_parent.telemetry_context,
                    log_level=log_level,
                )
            case TelemetryProvider.NULL:
                return NullTelemetry(
                    telemetry_context=self.telemetry_parent.telemetry_context
                )
            case _:
                raise ValueError("Invalid telemetry provider")

    def create_telemetry_span_creator(
        self, *, log_level: Optional[str | int]
    ) -> TelemetrySpanCreator:
        """
        Create a telemetry span creator

        :return: telemetry span creator
        """
        return TelemetrySpanCreator(
            telemetry=self.create(log_level=log_level),
        )

    # noinspection PyTypeChecker
    def __getstate__(self) -> Dict[str, Any]:
        raise NotImplementedError(
            "Serialization of TelemetrySpanCreator is not supported.  Did you accidentally try to send this object to a Spark worker?"
        )
