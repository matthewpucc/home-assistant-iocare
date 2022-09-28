""" DataUpdateCoordinator for the Coway integration. """
from __future__ import annotations

from datetime import timedelta

from cowayaio import CowayClient
from cowayaio.exceptions import AuthError, CowayError
from cowayaio.purifier_model import PurifierData


from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_USERNAME, CONF_PASSWORD
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import ConfigEntryAuthFailed
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed

from .const import DEFAULT_SCAN_INTERVAL, DOMAIN, LOGGER, TIMEOUT


class CowayDataUpdateCoordinator(DataUpdateCoordinator):
    """ Coway Data Update Coordinator. """

    data: PurifierData

    def __init__(self, hass: HomeAssistant, entry: ConfigEntry) -> None:
        """ Initialize the Coway coordinator. """

        self.hass = hass
        self.entry = entry
        self.entry_data = entry.data
        self.client = CowayClient(
            self.entry_data[CONF_USERNAME],
            self.entry_data[CONF_PASSWORD],
            session=async_get_clientsession(self.hass),
            timeout=TIMEOUT,
        )
        super().__init__(
            hass,
            LOGGER,
            name=DOMAIN,
            update_interval=timedelta(seconds=DEFAULT_SCAN_INTERVAL),
        )

    async def _async_update_data(self) -> PurifierData:
        """Fetch data from Coway.
        After the config entry is created for the first time,the initial
        coordinator update needs to reuse the access and refresh tokens
        obtained via the async_validate_api method. If not, Coway servers
        don't return an auth code. After the first data fetch, the initial
        access and refresh tokens can be removed from the config entry.
        """
        
        if 'initial_access_token' in self.entry_data:
            self.client.access_token = self.entry.data['initial_access_token']
            self.client.refresh_token = self.entry.data['initial_refresh_token']
            try:
                data = await self.client.async_get_purifiers_data()
            except AuthError as error:
                raise ConfigEntryAuthFailed from error
            except CowayError as error:
                raise UpdateFailed(error) from error

            if not data.purifiers:
                raise UpdateFailed("No Purifiers found")
            self.hass.config_entries.async_update_entry(
                self.entry,
                data={
                    CONF_USERNAME: self.entry_data[CONF_USERNAME],
                    CONF_PASSWORD: self.entry_data[CONF_PASSWORD],
                }
            )
            self.entry_data = {CONF_USERNAME: self.entry.data[CONF_USERNAME],CONF_PASSWORD: self.entry.data[CONF_PASSWORD]}
            return data
        else:
            try:
                data = await self.client.async_get_purifiers_data()
            except AuthError as error:
                raise ConfigEntryAuthFailed from error
            except CowayError as error:
                raise UpdateFailed(error) from error
            if not data.purifiers:
                raise UpdateFailed("No Purifiers found")
            return data
