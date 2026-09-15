"""Analytical mechanics model for a rectangular cantilever beam."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CantileverBeam:
    """Linear Euler-Bernoulli cantilever with a transverse tip load."""

    length_m: float
    width_m: float
    thickness_m: float
    youngs_modulus_pa: float

    @property
    def second_moment_area_m4(self) -> float:
        """Second moment of area about the neutral axis."""
        return self.width_m * self.thickness_m**3 / 12.0

    def tip_displacement_m(self, load_n: float) -> float:
        """Tip displacement magnitude for a transverse point load at the free end."""
        i = self.second_moment_area_m4
        return load_n * self.length_m**3 / (3.0 * self.youngs_modulus_pa * i)

    def root_bending_stress_pa(self, load_n: float) -> float:
        """Maximum bending stress magnitude at the fixed root."""
        return (
            6.0
            * load_n
            * self.length_m
            / (self.width_m * self.thickness_m**2)
        )

    def displacement_m(self, x_m: float, load_n: float) -> float:
        """Deflection magnitude along the beam for 0 <= x <= L."""
        if not 0.0 <= x_m <= self.length_m:
            raise ValueError("x_m must lie between 0 and the beam length.")

        i = self.second_moment_area_m4
        return (
            load_n
            * x_m**2
            * (3.0 * self.length_m - x_m)
            / (6.0 * self.youngs_modulus_pa * i)
        )

    def bending_stress_pa(self, x_m: float, load_n: float) -> float:
        """Maximum surface bending stress magnitude at axial location x."""
        if not 0.0 <= x_m <= self.length_m:
            raise ValueError("x_m must lie between 0 and the beam length.")

        moment_nm = load_n * (self.length_m - x_m)
        c_m = self.thickness_m / 2.0
        return moment_nm * c_m / self.second_moment_area_m4
