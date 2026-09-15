"""Run the first software-only cantilever digital twin demonstration."""

from cantilever_twin import CantileverBeam
from cantilever_twin.digital_twin import CantileverDigitalTwin


def main() -> None:
    beam = CantileverBeam(
        length_m=0.300,
        width_m=0.025,
        thickness_m=0.003,
        youngs_modulus_pa=68.9e9,
    )
    twin = CantileverDigitalTwin(beam)

    print("Cantilever Beam Digital Twin — Offline Demo")
    print("-" * 50)

    for load_n in (0.0, 2.5, 5.0, 7.5, 10.0):
        state = twin.update(load_n)
        print(
            f"Load: {state.load_n:5.1f} N | "
            f"Tip displacement: {state.tip_displacement_m * 1e3:8.3f} mm | "
            f"Root stress: {state.root_stress_pa / 1e6:8.3f} MPa"
        )


if __name__ == "__main__":
    main()
