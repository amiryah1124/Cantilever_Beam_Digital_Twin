# Cantilever Beam Digital Twin

A compact, physics-based digital twin demonstrator for a cantilever beam with live sensing, analytical/FEA state estimation, and real-time stress and deformation visualization.

## Project goal

Build and validate a semester-scale digital twin that connects a physical cantilever beam to a continuously updated digital representation. The final demonstrator will show live applied load, predicted tip displacement, stress, and deformation contours, and will be packaged as a reproducible GitHub project plus a technical demo/tutorial.

## Digital-twin architecture

```text
Physical Cantilever
      |
      v
Load Cell / Sensor
      |
      v
Arduino / ESP32
      |
      v
Python Data Acquisition
      |
      +--------------------+
      |                    |
      v                    v
Analytical Beam Model   FEA/ROM Model
      |                    |
      +---------+----------+
                |
                v
      Calibration / Validation
                |
                v
   Real-Time PyVista Visualization
                |
                v
 Stress + Deformation + Live Metrics
```

## Version 1 scope

- Rectangular aluminum cantilever beam
- Tip or near-tip transverse loading
- Load-cell measurement through Arduino/ESP32
- Euler-Bernoulli analytical reference model
- Reference finite-element solution from ANSYS
- Reduced-order real-time update of displacement/stress fields
- PyVista visualization of deformed shape and stress/deformation contours
- Experimental validation and model calibration
- Recorded LinkedIn demo and longer tutorial

## Why the first version is deliberately simple

The objective is to learn and demonstrate the complete digital-twin workflow rather than build a thesis-scale platform. Once the physical-to-digital pipeline works reliably, the same architecture can be extended to additively manufactured structures, anisotropic material behavior, manufacturing variability, embedded sensing, and data-assisted state estimation.

## Repository structure

```text
Cantilever_Beam_Digital_Twin/
├── config/                  # Beam, material, acquisition, and model settings
├── src/cantilever_twin/     # Reusable Python package
├── tests/                   # Unit tests
├── fea/                     # FEA workflow notes and exported reference fields
├── hardware/                # Sensor, wiring, microcontroller, and fixture notes
├── data/                    # Experimental/raw/processed data guidance
├── notebooks/               # Validation and exploratory analysis
├── docs/                    # Architecture, theory, roadmap, validation notes
├── media/                   # Figures, photos, and final demo assets
├── pyproject.toml
└── README.md
```

## Planned workflow

1. Define beam geometry, material properties, and loading.
2. Validate analytical tip displacement and root bending stress.
3. Build and verify a static ANSYS model.
4. Export a reference mesh and field solution.
5. Build PyVista stress/deformation visualization.
6. Connect live load-cell data through serial acquisition.
7. Update digital state in real time using a reduced-order physics model.
8. Compare analytical, FEA, and experimental results.
9. Calibrate the model and quantify prediction error.
10. Package the final demonstration, documentation, and tutorial.

## Core equations

For a cantilever beam with a tip load `P`:

```text
Tip displacement:       delta = P L^3 / (3 E I)
Root bending moment:    M = P L
Maximum bending stress: sigma_max = M c / I
```

For a rectangular cross-section:

```text
I = b h^3 / 12
sigma_max = 6 P L / (b h^2)
```

For a linear-elastic reference FEA solution computed at load `P0`, the first reduced-order implementation will use:

```text
u(P)     = (P/P0) * u0
sigma(P) = (P/P0) * sigma0
```

This avoids re-solving the full finite-element model at every sensor update while preserving the spatial field information for the linear regime.

## Milestone target

**Fall 2026:** working physical demonstrator, validated digital model, public GitHub repository, short LinkedIn demo, and a 5-10 minute technical tutorial.

## Status

Project initialized. Current focus: analytical model + offline digital twin before hardware integration.

## Author

Amir Abbas Yahyaeian
