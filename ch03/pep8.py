"""This script shows a few PEP 8 rules.
"""

import datetime as dt

from dateutil import tz


TEMPERATURE_SCALES = ('fahrenheit', 'kelvin',
                      'celsius')


class DummyClass:
    pass  # doesn't do anything at the moment


def convert_to_celsius(degrees, source='fahrenheit'):
    """This function converts degrees Fahrenheit or Kelvin
    into degrees Celsius.
    """
    if source.lower() == 'fahrenheit':
        return (degrees-32) * 5/9
    elif source.lower() == 'kelvin':
        return degrees - 273.15
    else:
        return f"Don't know how to convert from {source}"


celsius = convert_to_celsius(44, source='fahrenheit')
non_celcius_scales = TEMPERATURE_SCALES[:-1]

print('Current time: ' + dt.datetime.now(tz.UTC).isoformat())
print(f'The temperature in Celsius is: {celsius}')
