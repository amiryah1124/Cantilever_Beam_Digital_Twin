# Hardware

## Version 1 hardware concept

- Rectangular aluminum cantilever specimen
- Rigid clamp/fixture at one end
- Load cell for applied-force measurement
- HX711 load-cell amplifier
- Arduino or ESP32 for data acquisition
- USB serial connection to the host computer
- Independent displacement measurement for validation (dial indicator, digital indicator, or comparable method)

## Design priorities

1. Keep the fixture mechanically rigid relative to the beam.
2. Apply load at a repeatable location.
3. Keep expected loads inside the load-cell range.
4. Calibrate the load cell before structural validation.
5. Record specimen dimensions with sufficient precision for analytical/FEA comparison.

## Planned files

- `wiring/` — wiring diagrams and pin assignments
- `firmware/` — Arduino/ESP32 code
- `fixture/` — fixture drawings/photos
- `calibration/` — load-cell calibration records

Do not commit sensitive machine-specific serial-port settings or large raw recordings to the repository.
