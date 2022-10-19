import requests

def get_weather():
    api_key = "7fdf17f869502f73eae7841656d57753"
    city = "Ogden"

    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"
    data = requests.get(url).json()

    description = data.get("weather")[0].get("description")
    temp_min = data.get("main").get("temp_min")
    temp_max = data.get("main").get("temp_max")

    return {
    'description': description, 
    'temp_min': temp_min, 
    'temp_max': temp_max,
    'city': city
    }

def main():
    # Print the results
    weather_dict = get_weather()
    print("Today's forecast in", weather_dict.get('city'), "is", weather_dict.get('description'))
    print("The minimum temperature is", weather_dict.get('temp_min'))
    print("The minimum temperature is", weather_dict.get('temp_max'))

main()