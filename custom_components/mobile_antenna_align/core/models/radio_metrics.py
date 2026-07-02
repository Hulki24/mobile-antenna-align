"""Common radio data model."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True)
class RadioMetrics:
    """Manufacturer-independent radio metrics."""

    technology: str | None = None

    manufacturer: str | None = None
    model: str | None = None
    provider: str | None = None

    serial_number: str | None = None
    firmware: str | None = None

    # LTE

    lte_rsrp: int | None = None
    lte_rsrq: int | None = None
    lte_rssi: int | None = None

    lte_band: str | None = None
    lte_cell_id: str | None = None
    lte_pci: int | None = None

    # NR

    nr_rsrp: int | None = None
    nr_rsrq: int | None = None
    nr_rssi: int | None = None

    nr_band: str | None = None
    nr_cell_id: str | None = None

    distance: int | None = None