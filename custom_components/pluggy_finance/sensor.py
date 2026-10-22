"""Sensor platform for Pluggy Finance."""
from __future__ import annotations

from homeassistant.components.sensor import SensorEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN


async def async_setup_entry(
    hass: HomeAssistant,
    config_entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up Pluggy Finance sensors from a config entry."""
    async_add_entities([])


class PluggyFinanceSensor(SensorEntity):
    """Representation of a Pluggy Finance sensor."""

    _attr_has_entity_name = True
    _attr_name = "Pluggy Finance"

    def __init__(self, unique_id: str) -> None:
        self._attr_unique_id = unique_id

    @property
    def native_value(self):
        """Return the state of the sensor."""
        return None
