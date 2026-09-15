# Finite-Element Model

## Version 1 solver

ANSYS Mechanical static structural analysis.

## Required model definition

- Geometry identical to the measured physical specimen
- Linear-elastic isotropic material model
- Fixed support at the clamped end
- Transverse point or distributed load applied at the experimental load location
- Mesh refinement near the fixed root and load application region

## Verification tasks

- Check reaction force balance.
- Perform a basic mesh-convergence study.
- Compare tip displacement against Euler-Bernoulli theory.
- Compare root bending stress away from fixture singularities with analytical stress.
- Define a reference load `P0` for exported displacement/stress fields.

## Reference-field export

The real-time twin will initially use a linear reduced-order model:

```text
u(P)     = (P/P0) * u0
sigma(P) = (P/P0) * sigma0
```

Exported mesh and scalar/vector fields should be stored in `fea/reference_results/` locally. Large solver-generated files are intentionally excluded from Git.
