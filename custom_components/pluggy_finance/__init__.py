
"""Integração Pluggy Finance para Home Assistant."""

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

async def async_setup(hass: HomeAssistant, config: dict) -> bool:
    """Configuração inicial da integração."""
    return True

async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry
) -> bool:
    """Configura uma entrada da integração."""
    return True

async def async_unload_entry(
    hass: HomeAssistant, entry: ConfigEntry
) -> bool:
    """Descarrega uma entrada da integração."""
    return True
