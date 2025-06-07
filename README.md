![sample screenshot](https://github.com/Carlbern/polybar-weather/blob/master/Screenshot%20from%202025-06-07%2017-38-06.png)


Small script that displays current temperature of a location. 

The default location is Paris, France. 

To change location, simply change the input of the function on the last line.

To change from celsius to farenhet, comment out the line with "OUTPUT FORMAT CELSIUS" and uncomment the "OUTPUT FORMAT FARENHEIT"

### Dependencies
-GeoPy


### Settings
``` ini
[module/weather]
type = custom/script
exec = python3 Path/To/Script/polybar-weather.py
interval = 10
```
