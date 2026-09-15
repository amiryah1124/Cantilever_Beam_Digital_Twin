# Fall 2026 Roadmap

## Phase 1 — Mechanics and offline twin
**Target: September 2026**

- Freeze Version 1 beam geometry and material.
- Derive and verify analytical equations.
- Run parameter checks for expected load/displacement/stress ranges.
- Build static ANSYS model.
- Perform basic mesh-convergence study.
- Compare analytical and FEA tip displacement/root stress.

**Exit criterion:** analytical and FEA predictions agree within a justified tolerance.

## Phase 2 — Real-time software twin
**Target: early October 2026**

- Export ANSYS mesh/reference displacement and stress fields.
- Implement reference-field import.
- Implement linear-elastic reduced-order scaling.
- Build PyVista deformation/stress visualization.
- Drive the twin first with a simulated load signal.

**Exit criterion:** a software-only load input updates live contours and numerical metrics.

## Phase 3 — Physical sensing
**Target: late October 2026**

- Assemble cantilever fixture.
- Integrate load cell + HX711 + Arduino/ESP32.
- Calibrate force measurement.
- Stream force data to Python.
- Add filtering and basic fault handling.

**Exit criterion:** physical loading updates the digital twin reliably in real time.

## Phase 4 — Validation and calibration
**Target: November 2026**

- Measure tip displacement independently.
- Run multiple loading/unloading trials.
- Compare analytical, FEA, twin, and experimental values.
- Quantify error and repeatability.
- Estimate an effective stiffness/correction factor if needed.

**Exit criterion:** documented validation plots and quantified model error.

## Phase 5 — Portfolio release
**Target: late November / early December 2026**

- Clean repository and documentation.
- Add wiring/architecture diagrams and photos.
- Record a 60–90 second LinkedIn demo.
- Record a 5–10 minute technical tutorial.
- Document how the architecture extends to additive-manufactured structures.

**Final success criterion:** public, reproducible physical digital-twin demonstrator with a concise technical story.

## Scope guardrails

Version 1 will not include cloud IoT infrastructure, machine learning, NVIDIA Omniverse, nonlinear material models, fatigue prediction, thermal coupling, or full closed-loop control. Those are optional future extensions only after the core demonstrator is complete.
