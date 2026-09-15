# System Architecture

## Objective

Create a small but complete physical-to-digital structural monitoring loop that is easy to understand, validate, demonstrate, and extend.

## Data flow

1. A physical cantilever beam is loaded.
2. A load cell measures the applied force.
3. Arduino/ESP32 streams the measured load to the computer.
4. Python acquires and filters the signal.
5. The digital twin converts the load into structural state estimates.
6. Analytical mechanics provides an independent baseline.
7. A reference finite-element solution provides spatial displacement and stress fields.
8. A linear-elastic reduced-order model scales those fields in real time.
9. PyVista displays live deformation/stress contours and numerical metrics.
10. Experimental measurements are compared against the predicted state for validation/calibration.

## Software boundaries

- `analytical_model.py`: closed-form structural mechanics
- `acquisition.py`: simulated or serial sensor input
- `digital_twin.py`: current structural state
- `rom.py`: reference FEA field scaling
- future `visualization.py`: PyVista rendering and live updates
- future `calibration.py`: model-to-experiment parameter correction

## Design principle

The hardware, physics model, reduced-order model, and visualization should remain loosely coupled. This allows later replacement of the simple aluminum cantilever with an additively manufactured structure without rebuilding the entire software stack.
