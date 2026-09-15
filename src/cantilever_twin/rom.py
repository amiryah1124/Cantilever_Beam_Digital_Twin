"""Reduced-order scaling of a linear-elastic reference FEA solution."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ReferenceField:
    """Reference finite-element fields evaluated at a known applied load."""

    reference_load_n: float
    displacement_m: np.ndarray
    stress_pa: np.ndarray

    def scaled(self, load_n: float) -> tuple[np.ndarray, np.ndarray]:
        """Scale reference displacement and stress fields for linear elasticity."""
        if self.reference_load_n == 0.0:
            raise ValueError("reference_load_n must be nonzero.")

        scale = float(load_n) / self.reference_load_n
        return self.displacement_m * scale, self.stress_pa * scale
