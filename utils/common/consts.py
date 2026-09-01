from homeassistant.components.binary_sensor import BinarySensorDeviceClass
from homeassistant.const import Platform

CUSTOM_PARAMETERS = [
    {
        "key": "Power",
        "name": "Power",
        "platform": str(Platform.BINARY_SENSOR),
        "device_class": str(BinarySensorDeviceClass.POWER),
        "on_value": "1"
    },
    {
        "key": "Mode",
        "name": "Mode",
        "platform": None
    },
    {
        "key": "Manual-mute",
        "name": "Manual-mute",
        "platform": None
    },
    {
        "key": "Set_Temp",
        "name": "Set_Temp",
        "platform": None
    },
    {
        "key": "2074",
        "name": "2074",
        "platform": None
    },
    {
        "key": "2075",
        "name": "2075",
        "platform": None
    },
    {
        "key": "2076",
        "name": "2076",
        "platform": None
    },
    {
        "key": "2077",
        "name": "2077",
        "platform": None
    },
    {
        "key": "1158",
        "name": "1158",
        "platform": None
    },
    {
        "key": "1159",
        "name": "1159",
        "platform": None
    },
    {
        "key": "2064",
        "name": "2064",
        "platform": None
    },
    {
        "key": "ver",
        "name": "Version",
        "platform": None
    },
    {
        "key": "software_code",
        "name": "Software Code",
        "platform": None
    },
]

# Promotion is a semantic judgement, not derivable from resources.xml, so it is
# re-applied here after generation to keep regeneration idempotent.
PROMOTED_PARAMETERS = {
    "default": {
        "T02": {"entity_category": None, "state_class": "measurement"},
        "T03": {"entity_category": None, "state_class": "measurement"},
        "T05": {"entity_category": None, "state_class": "measurement"},
    },
    "device_1442284873216843776": {
        "T2": {"entity_category": None, "state_class": "measurement"},
        "T3": {"entity_category": None, "state_class": "measurement"},
        "T5": {"entity_category": None, "state_class": "measurement"},
    },
}
