import requests
from geopy.geocoders import Nominatim

def get_weather(city):
    #GET LOCATION COORDINATES
    nomAgent = Nominatim(user_agent="location")
    location = nomAgent.geocode(city).raw

    #API REQUEST
    url = "https://api.open-meteo.com/v1/forecast?latitude=" + location["lat"] + "&longitude=" + location["lon"] + "&current=temperature_2m"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        current_temp_c = data["current"]["temperature_2m"] 
        current_temp_f = ((current_temp_c * 1.8) + 32) 


        if current_temp_c > 22:
            icon = " "
        elif current_temp_c > 15:
            icon = " "
        elif current_temp_c > 10:
            icon = " "
        elif current_temp_c > 5:
            icon = " "
        else:
            icon = " " 

        #OUTPUT FORMAT CELSIUS
        return  icon + str(current_temp_c) + "°C"

        #OUTPUT FORMAT FARENHEIT
        #return " " + str(current_temp_f) + "°F"
    
    else:
        return None
    
#INPUT LOCATION HERE
print(get_weather("Paris")) 


