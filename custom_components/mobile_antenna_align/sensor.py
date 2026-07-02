"""Sensor platform for HA FRITZ!Box Mobile."""

from __future__ import annotations

from dataclasses import dataclass

from homeassistant.components.sensor import (
    SensorEntity,
    SensorEntityDescription,
)
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import (
    SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
)
from homeassistant.core import HomeAssistant
from homeassistant.helpers.device_registry import DeviceInfo
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import CoordinatorEntity

from .const import (
    DOMAIN,
    MANUFACTURER,
    DEFAULT_MODEL,
    PROJECT_NAME,
)
from .coordinator import Fritz5GCoordinator


@dataclass(frozen=True, kw_only=True)
class Fritz5GSensorDescription(SensorEntityDescription):
    """FRITZ!Box Mobile sensor description."""

    value_key: str


SENSORS: tuple[Fritz5GSensorDescription, ...] = (
    Fritz5GSensorDescription(
        key="technology",
        name="Technology",
        value_key="technology",
    ),
    Fritz5GSensorDescription(
        key="provider",
        name="Provider",
        value_key="provider",
    ),
    Fritz5GSensorDescription(
        key="lte_rsrp",
        name="LTE RSRP",
        value_key="lte_rsrp",
        native_unit_of_measurement=SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
    ),
    Fritz5GSensorDescription(
        key="lte_rsrq",
        name="LTE RSRQ",
        value_key="lte_rsrq",
        native_unit_of_measurement="dB",
    ),
    Fritz5GSensorDescription(
        key="lte_rssi",
        name="LTE RSSI",
        value_key="lte_rssi",
        native_unit_of_measurement=SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
    ),
    Fritz5GSensorDescription(
        key="nr_rsrp",
        name="NR RSRP",
        value_key="nr_rsrp",
        native_unit_of_measurement=SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
    ),
    Fritz5GSensorDescription(
        key="nr_rsrq",
        name="NR RSRQ",
        value_key="nr_rsrq",
        native_unit_of_measurement="dB",
    ),
    Fritz5GSensorDescription(
        key="nr_rssi",
        name="NR RSSI",
        value_key="nr_rssi",
        native_unit_of_measurement=SIGNAL_STRENGTH_DECIBELS_MILLIWATT,
    ),
    Fritz5GSensorDescription(
        key="lte_pci",
        name="PCI",
        value_key="lte_pci",
    ),
    Fritz5GSensorDescription(
        key="distance",
        name="Distance",
        value_key="distance",
        native_unit_of_measurement="m",
    ),
    Fritz5GSensorDescription(
        key="lte_cell_id",
        name="LTE Cell ID",
        value_key="lte_cell_id",
    ),
)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up FRITZ!Box Mobile sensors."""

    coordinator: Fritz5GCoordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities(
        Fritz5GSensor(coordinator, description)
        for description in SENSORS
    )


class Fritz5GSensor(
    CoordinatorEntity[Fritz5GCoordinator],
    SensorEntity,
):
    """FRITZ!Box Mobile sensor."""

    entity_description: Fritz5GSensorDescription

    def __init__(
        self,
        coordinator: Fritz5GCoordinator,
        description: Fritz5GSensorDescription,
    ) -> None:
        """Initialize sensor."""

        super().__init__(coordinator)

        self.entity_description = description

        self._attr_unique_id = (
            f"{coordinator.config_entry.entry_id}_{description.key}"
        )

        self._attr_has_entity_name = True
        
        self._attr_device_info = DeviceInfo(
            identifiers={
                (
                    DOMAIN,
                    coordinator.data.serial_number or "unknown",
                )
    },
    manufacturer=MANUFACTURER,
    model=coordinator.data.model or DEFAULT_MODEL,
    name=coordinator.data.friendly_name or DEFAULT_MODEL,
    serial_number=coordinator.data.serial_number,
    sw_version=coordinator.data.firmware,
)
        

    @property
    def native_value(self):
        """Return sensor value."""

        return getattr(
            self.coordinator.data,
            self.entity_description.value_key,
            None,
        )
        
   
        
        
#Ende