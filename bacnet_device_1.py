
from time import sleep
import random
from BAC0.core.devices.local.object import ObjectFactory
from bacpypes.object import ScheduleObject
from bacpypes.primitivedata import Real
from BAC0 import lite, connect
from BAC0.core.devices.local.models import (
    analog_input, analog_output,
    binary_output, binary_input,
    )


def display(elements):
    print(elements['properties']['presentValue'])


# Define device objects
def defining_objects(device):
    # start from fresh
    ObjectFactory.clear_objects()
    # content of the object is defined here onwards.
    objets = analog_input(
        instance=1,
        name="Frequency",
        properties={"units": "hertz"},
        description="Frequency",
        presentValue=18.0,
    )
    analog_input(
        instance=2,
        name="Barometer",
        properties={"units": "pascals"},
        description="Room Pressure",
        presentValue=19.0,
    )
    analog_input(
        instance=3,
        name="Humidity",
        properties={"units": "degreesCelsius"}, description="Room Humidity",
        presentValue=21,
        relinquish_default=21
    )
    analog_input(
        instance=4,
        name="Temperature",
        properties={"units": "degreesCelsius"},
        description="Room Temperature",
        presentValue=20, relinquish_default=20
    )
    analog_output(
        instance=5,
        name="Gas resistence",
        properties={"units": "degreesCelsius"},
        description="Room two set point",
        presentValue=20,
        relinquish_default=20
    )
    binary_output(
        instance=10,
        name="RoomOneHeatingEnabled",
        description="Room one heating enabled", presentValue=True,
    )
    binary_output(
        instance=11,
        name="Room TwoHeatingEnabled", description="Room two heating enabled",
        presentValue=True,
    )
    binary_input(
        instance=12,
        name="RoomOneRadiatorState",
        description="Room one radiator on/off", presentValue=False,
    )
    binary_input(
        instance=13,
        name="RoomTwoRadiatorState",
        description="Room two radiator on/off", presentValue=False,
    )
    return objets.add_objects_to_application(device)


# Define device
device1 = lite()
defining_objects(device1)

while True:
    device1["Frequency"].presentValue = random.uniform(5, 100)
    device1["Temperature"].presentValue = random. uniform(5, 100)
    sleep(1)
