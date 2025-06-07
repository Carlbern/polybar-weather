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
        current_temp = data["current"]["temperature_2m"] 

        #OUTPUT FORMAT
        return " " + str(current_temp) + "°C"
    else:
        return None
    
#INPUT LOCATION HERE
print(get_weather("Paris")) 


