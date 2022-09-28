""" Utilities for Coway Integration """
from __future__ import annotations

import async_timeout
from cowayaio import CowayClient
from cowayaio.exceptions import AuthError, CowayError

from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import LOGGER, COWAY_ERRORS, TIMEOUT

async def async_validate_api(hass: HomeAssistant, username: str, password: str) -> bool:
    """ Get data from API. """

    client = CowayClient(
        username,
        password,
        session=async_get_clientsession(hass),
        timeout=TIMEOUT,
    )

    try:
        async with async_timeout.timeout(TIMEOUT):
            coway_query = await client.async_get_purifiers()
    except AuthError as err:
        LOGGER.error(f'Could not authenticate on Coway servers: {err}')
        raise AuthError from err
    except COWAY_ERRORS as err:
        LOGGER.error(f'Failed to get information from Coway servers: {err}')
        raise ConnectionError from err
    purifiers: list = coway_query['body']['deviceInfos']
    if not purifiers:
        LOGGER.error("Could not retrieve any purifiers from Coway servers")
        raise NoPurifiersError
    else:
        return client.access_token, client.refresh_token


class NoPurifiersError(Exception):
    """ No Purifiers from Coway API. """
