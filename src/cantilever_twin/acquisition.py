"""Sensor acquisition interfaces for simulated and serial load data."""

from __future__ import annotations

import time
from dataclasses import dataclass
from typing import Iterator


@dataclass
class SimulatedLoadSource:
    """Simple deterministic load source for software-only development."""

    loads_n: list[float]
    interval_s: float = 0.1

    def stream(self) -> Iterator[float]:
        for load_n in self.loads_n:
            yield float(load_n)
            time.sleep(self.interval_s)


class SerialLoadSource:
    """Read one numeric load value per line from a serial-connected controller."""

    def __init__(self, port: str, baud_rate: int = 115200, timeout_s: float = 1.0):
        try:
            import serial
        except ImportError as exc:
            raise RuntimeError("pyserial is required for serial acquisition.") from exc

        self._serial = serial.Serial(port=port, baudrate=baud_rate, timeout=timeout_s)

    def read_load_n(self) -> float:
        line = self._serial.readline().decode("utf-8").strip()
        if not line:
            raise TimeoutError("No load value received before serial timeout.")
        return float(line)

    def close(self) -> None:
        if self._serial.is_open:
            self._serial.close()
