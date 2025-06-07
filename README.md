Small script that displays current temperature of a location.

The default location is Paris, France.

To change location, simply change the input of the function on the last line.

To change from celsius to farenhet, comment out the line with "OUTPUT FORMAT CELSIUS" and uncomment the "OUTPUT FORMAT FARENHEIT"

DEPENDENCIES:

    GeoPy
        install with either:
            pip install geopy
            sudo apt install python3-geopy

            or similar commands for your distribution

    FontAwesome
        The icon uses FontAwesome icon font

:
[module/weather]
type = custom/script
exec = python3 Path/To/Script/polybar-weather.py
interval = 10
:
