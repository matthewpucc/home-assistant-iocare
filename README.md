# Coway IoCare Home Assistant Integration - 300S & 400S
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration) ![GitHub manifest version (path)](https://img.shields.io/github/manifest-json/v/RobertD502/home-assistant-iocare?filename=custom_components%2Fcoway%2Fmanifest.json)

<a href="https://www.buymeacoffee.com/RobertD502" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="100" width="424"></a>

### A lot of work has been put into creating the backend and this integration. If you enjoy this integration, consider donating by clicking on the logo above.

***All proceeds go towards helping a local animal rescue.**


# Notice (10/25/22)
Coway is requiring users to transfer their accounts to a Coway account which has broken this integration. I am currently working on determining their new authorization method which will need to be implemented into the backend. Once finished, a new update will be released and this notice removed.
## Installation

An account (E-mail/Password) created directly through Coway is required. If you use any of the third-party options (Facebook, Google, Apple, Kakao, Line) to sign in to the IoCare app, this integration will not work.  

### With HACS
This integration is part of the HACS default repo.

1. Go to the HACS integrations page and select `+ EXPLORE & DOWNLOAD REPOSITORIES` (lower right-hand corner)
2. Search for `Coway` and select it.
3. Select `Download` (lower right-hand corner)
4. Select `Download` once again
5. Restart Home Assistant
6. Follow the instructions in the `Setup` section

### Manual
1. Copy the `coway` directory from `custom_components` in this repository and place inside your Home Assistant's `custom_components` directory.
2. Restart Home Assistant
3. Follow the instructions in the `Setup` section

`Note`: If installing manually, in order to be alerted about new releases, you will need to subscribe to releases from this repository. 

## Setup
Navigate to Settings > Devices & Services > click the `+ Add Integration` button > search for "Coway" (restart Home Assistant and / or clear browser cache if you can't find it)

Alternatively, click on the button below to add the integration:

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=coway)

# Devices

## Note

Coway is shipping new 400S (possibly also 300S) units, which are not reporting AQI. 

**The AQI sensor entity is not available for these new units.**

If/when Coway's servers start reporting AQI values, AQI sensor entities will be made available.


#

Each purifier is exposed as a device in Home Assistant.

Each purifier has the following entities:



| Entity | Entity Type | Additional Comments |
| --- | --- | --- |
| `Purifier` | `Fan` | Ability of controlling power, speed, and preset mode (Auto Mode, Night Mode) |
| `Current timer` | `Select` | Ability to set timer to OFF, 1 hour, 2 hours, 4 hours, or 8 hours. `Setting a timer can only be done when a purifier is powered ON` |
| `Light` | `Switch` | Ability to turn light on and off. `Controlling the light can only be done when a purifier is powered ON` |
| `AQI` | `Sensor` | Air Quality Index |
| `MAX2 Filter` | `Sensor` | Percentage of MAX2 filter life remaining |
| `Pre Filter` | `Sensor` | Percentage of Pre filter remaining |
| `Particulate Matter 10` | `Sensor` | |
| `Timer remaining` | `Sensor` | Shows the current amount of time left on a timer. This is a string in the form of hours:minutes |

