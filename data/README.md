# Data

Keep experimental data organized by acquisition stage.

Suggested local structure:

```text
data/
├── raw/          # Unmodified sensor captures
├── processed/    # Cleaned/calibrated data
└── validation/   # Curated comparison datasets
```

Each validation dataset should record, at minimum: date, specimen dimensions, material assumption, load location, sensor calibration version, sampling rate, applied load, measured displacement, and notes about the fixture/setup.

Large raw files are excluded from Git by default. Small curated CSV files used to reproduce published figures may be committed later.
