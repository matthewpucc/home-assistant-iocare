""" Constants for Coway """

import asyncio
import logging

from aiohttp.client_exceptions import ClientConnectionError

from homeassistant.const import Platform
from homeassistant.util.percentage import ordered_list_item_to_percentage

from cowayaio.exceptions import AuthError, CowayError

LOGGER = logging.getLogger(__package__)

DEFAULT_SCAN_INTERVAL = 30
DOMAIN = "coway"
PLATFORMS = [
    Platform.FAN,
    Platform.SELECT,
    Platform.SENSOR,
    Platform.SWITCH,
]

DEFAULT_NAME = "Coway IoCare"
TIMEOUT = 20

COWAY_ERRORS = (
    asyncio.TimeoutError,
    ClientConnectionError,
    AuthError,
    CowayError,
)


IOCARE_FAN_OFF = "0"
IOCARE_FAN_LOW = "1"
IOCARE_FAN_MEDIUM = "2"
IOCARE_FAN_HIGH = "3"

IOCARE_TIMER_OFF = "0"
IOCARE_TIMER_1H = "60"
IOCARE_TIMER_2H = "120"
IOCARE_TIMER_4H = "240"
IOCARE_TIMER_8H = "480"

IOCARE_TIMERS = ["OFF", "1 Hour", "2 Hours", "4 Hours", "8 Hours"]
IOCARE_TIMERS_TO_HASS = {
    IOCARE_TIMER_OFF: "OFF",
    IOCARE_TIMER_1H: "1 Hour",
    IOCARE_TIMER_2H: "2 Hours",
    IOCARE_TIMER_4H: "4 Hours",
    IOCARE_TIMER_8H: "8 Hours"
}

PRESET_MODE_AUTO = "Auto"
PRESET_MODE_NIGHT = "Night"

ORDERED_NAMED_FAN_SPEEDS = [IOCARE_FAN_LOW, IOCARE_FAN_MEDIUM, IOCARE_FAN_HIGH]
PRESET_MODES = [PRESET_MODE_AUTO, PRESET_MODE_NIGHT]

IOCARE_FAN_SPEED_TO_HASS = {
    IOCARE_FAN_OFF: 0,
    IOCARE_FAN_LOW: ordered_list_item_to_percentage(ORDERED_NAMED_FAN_SPEEDS, IOCARE_FAN_LOW),
    IOCARE_FAN_MEDIUM: ordered_list_item_to_percentage(ORDERED_NAMED_FAN_SPEEDS, IOCARE_FAN_MEDIUM),
    IOCARE_FAN_HIGH: ordered_list_item_to_percentage(ORDERED_NAMED_FAN_SPEEDS, IOCARE_FAN_HIGH)
}
