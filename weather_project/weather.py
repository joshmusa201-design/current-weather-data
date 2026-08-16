#this is a weather app that tells you temperature etc

import requests

url = "https://api.open-meteo.com/v1/forecast"

urlu = "https://geocoding-api.open-meteo.com/v1/search"

user_name = input("enter your name: ")

print("welcome", user_name)

country = input("Enter a country: ")
city = input("Enter a city: ")

results = {
    "name":city,
    "country": country,
    "admin1" : city,
    "timezone": "auto",
    "admin2": city,
    "admin3": city,
}
try:
    response = requests.get(urlu, results)
    me = response.json()
    filter = me["results"][0]
    latitude = filter["latitude"]
    longitude= filter["longitude"]
    timezone = filter["timezone"]
 

    # the parameters for the api calling
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "timezone": timezone,
        "current": 
        ["temperature_2m",
        "relative_humidity_2m",
        "wind_speed_10m",
        "weather_code"
        ],
    }

    #getting the api to get the data from the weather server
    response = requests.get(url, params)
    bottle = response.json()

    current = bottle["current"]

    weather_code = current["weather_code"]


    #printing the api respose
    print("CURRENT WEATHER")
    print()
    print(f"Temperature: {current["temperature_2m"]}℃")
    print(f"Humidity: {current["relative_humidity_2m"]}%")
    print(f"Wind speed: {current["wind_speed_10m"]}km/h")

    #modifying the WMO to english(alphabet)
    if weather_code == 0:
        print("Condition: Clear Sky ")
    elif weather_code == 1 or weather_code == 2 or weather_code == 3:
        print("Condition: Mainly clear, Partly cloudy, and Overcast ⛅")
    elif weather_code == 45 or weather_code == 48:
        print("Condition: fog and depositing rime fog 😶‍🌫️")
    elif weather_code == 51 or weather_code == 53 or weather_code == 55:
        print("Condition: Drizzle ")
    elif weather_code == 56 or weather_code == 57:
        print("Condition: Freezing Drizzle 🥶")
    elif weather_code == 61 or weather_code == 63 or weather_code == 65 or weather_code == 66 or weather_code == 67 or weather_code == 80 or weather_code == 81 or weather_code == 82: 
        print("Condition: Raining  🌧️")
    elif weather_code == 71 or weather_code == 73 or weather_code == 75 or weather_code == 77 or weather_code == 85 or weather_code == 86:
        print("Condition: Snow fall ❄️")

    print()
    print(f"{user_name}, thanks for using my weather forecast 😎❤️")

except KeyError:
    print("you haven't enter the country you want to search for")

#thanks for using this. JOSHUA ISHAYA MUSA