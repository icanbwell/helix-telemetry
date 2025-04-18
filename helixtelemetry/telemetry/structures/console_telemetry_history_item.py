import dataclasses
from typing import List

from dataclasses_json import DataClassJsonMixin

from helixtelemetry.telemetry.context.telemetry_context import TelemetryContext
from helixtelemetry.telemetry.structures.telemetry_parent import TelemetryParent


@dataclasses.dataclass
class ConsoleTelemetryHistoryItem(DataClassJsonMixin):
    context: TelemetryContext

    telemetry_parent: TelemetryParent

    name: str

    children: List["ConsoleTelemetryHistoryItem"] = dataclasses.field(
        default_factory=list
    )

    @classmethod
    def from_telemetry_context(
        cls,
        *,
        name: str,
        telemetry_context: TelemetryContext,
        telemetry_parent: TelemetryParent,
    ) -> "ConsoleTelemetryHistoryItem":
        return cls(
            context=telemetry_context,
            children=[],
            name=name,
            telemetry_parent=telemetry_parent,
        )
