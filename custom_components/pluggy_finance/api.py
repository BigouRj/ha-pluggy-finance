"""API client for Pluggy Finance."""
from __future__ import annotations

from typing import Any


class PluggyFinanceAPIClient:
    """Client for interacting with the Pluggy Finance API."""

    def __init__(self, api_key: str, base_url: str) -> None:
        self._api_key = api_key
        self._base_url = base_url.rstrip("/")

    async def async_get_data(self) -> dict[str, Any]:
        """Fetch data from the Pluggy Finance API."""
        # TODO: Implement API call to retrieve finance data.
        return {"status": "not_implemented"}
