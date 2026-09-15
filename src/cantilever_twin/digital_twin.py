"""Core state update logic for the cantilever digital twin."""

from __future__ import annotations

from dataclasses import dataclass

from .analytical_model import CantileverBeam


@dataclass(frozen=True)
class TwinState:
    load_n: float
    tip_displacement_m: float
    root_stress_pa: float


class CantileverDigitalTwin:
    """Minimal physics-based digital twin for the first project milestone."""

    def __init__(self, beam: CantileverBeam):
        self.beam = beam

    def update(self, load_n: float) -> TwinState:
        """Map the current measured load to the estimated structural state."""
        return TwinState(
            load_n=float(load_n),
            tip_displacement_m=self.beam.tip_displacement_m(load_n),
            root_stress_pa=self.beam.root_bending_stress_pa(load_n),
        )
