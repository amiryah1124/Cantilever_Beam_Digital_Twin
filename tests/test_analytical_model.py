import pytest

from cantilever_twin import CantileverBeam


def test_tip_displacement_matches_closed_form():
    beam = CantileverBeam(
        length_m=0.300,
        width_m=0.025,
        thickness_m=0.003,
        youngs_modulus_pa=68.9e9,
    )

    load_n = 10.0
    expected = load_n * beam.length_m**3 / (
        3.0 * beam.youngs_modulus_pa * beam.second_moment_area_m4
    )

    assert beam.tip_displacement_m(load_n) == pytest.approx(expected)


def test_root_stress_scales_linearly_with_load():
    beam = CantileverBeam(0.300, 0.025, 0.003, 68.9e9)

    stress_5n = beam.root_bending_stress_pa(5.0)
    stress_10n = beam.root_bending_stress_pa(10.0)

    assert stress_10n == pytest.approx(2.0 * stress_5n)


def test_fixed_end_displacement_is_zero():
    beam = CantileverBeam(0.300, 0.025, 0.003, 68.9e9)

    assert beam.displacement_m(0.0, 10.0) == pytest.approx(0.0)
