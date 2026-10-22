"""Coordinator for Pluggy Finance data updates."""
from __future__ import annotations

from datetime import timedelta

from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .api import PluggyFinanceAPIClient
from .const import DOMAIN


class PluggyFinanceCoordinator(DataUpdateCoordinator[dict]):
    """Manage fetching and updating Pluggy Finance data."""

    def __init__(self, hass: HomeAssistant, api_client: PluggyFinanceAPIClient) -> None:
        super().__init__(
            hass,
            logger=__import__("logging").getLogger(__name__),
            name=DOMAIN,
            update_interval=timedelta(minutes=5),
        )
        self.api_client = api_client

    async def _async_update_data(self) -> dict:
        """Fetch data from the API."""
        return await self.api_client.async_get_data()
