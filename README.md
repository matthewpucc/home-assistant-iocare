# Coway IoCare Home Assistant Integration - 300S & 400S
[![hacs_badge](https://img.shields.io/badge/HACS-Default-orange.svg)](https://github.com/hacs/integration) ![GitHub manifest version (path)](https://img.shields.io/github/manifest-json/v/RobertD502/home-assistant-iocare?filename=custom_components%2Fcoway%2Fmanifest.json)

<a href="https://www.buymeacoffee.com/RobertD502" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="100" width="424"></a>

### A lot of work has been put into creating the backend and this integration. If you enjoy this integration, consider donating by clicking on the logo above.

***All proceeds go towards helping a local animal rescue.**

Home Assistant custom component for monitoring and controlling Coway Airmega air purifiers.




## Installation

An account (E-mail/Password) created directly through Coway is required. If you use any of the third-party options (Facebook, Google, Apple, Kakao, Line) to sign in to the IoCare app, this integration will not work.  

### With HACS
1. Open HACS Settings and add this repository (https://github.com/RobertD502/home-assistant-iocare)
as a Custom Repository (use **Integration** as the category).
2. The `Coway IoCare` page should automatically load (or find it in the HACS Store)
3. Click `Install`

### Manual
Copy the `coway` directory from `custom_components` in this repository,
and place inside your Home Assistant Core installation's `custom_components` directory.

`Note`: If installing manually, in order to be alerted about new releases, you will need to subscribe to releases from this repository. 

## Setup
1. Install this integration.
2. Use Config Flow to configure the integration with your Coway IoCare credentials.
    * Initiate Config Flow by navigating to Configuration > Integrations > click the "+" button > find "Coway IoCare" (restart Home Assistant and / or clear browser cache if you can't find it)

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
| `Current Timer` | `Select` | Ability to set timer to OFF, 1 hour, 2 hours, 4 hours, or 8 hours |
| `Purifier Light` | `Switch` | Ability to turn light on and off |
| `AQI` | `Sensor` | Air Quality Index |
| `Carbon Dioxide` | `Sensor` | |
| `MAX2 Filter` | `Sensor` | Percentage of MAX2 filter life remaining |
| `Pre Filter` | `Sensor` | Percentage of Pre filter remaining |
| `Particulate Matter 10` | `Sensor` | |
| `Particulate Matter 2.5` | `Sensor` | |
| `VOC` | `Sensor` | |
| `Timer Remaining` | `Sensor` | Shows the current amount of time left on a timer. This is a string in the form of hours:minutes |

