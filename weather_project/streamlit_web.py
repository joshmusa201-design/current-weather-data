import requests

import streamlit as st
st.title("JOSH WEATHER WEBSITE")
with st.form(key="MY WEATHER APP"):
    country = st.text_input("Enter The Name Of The Country")
    city = st.text_input("Enter The Name Of The City ")
    submit_buttin = st.form_submit_button("GET WEATHER")
    url = "https://api.open-meteo.com/v1/forecast"
    urlu = "https://geocoding-api.open-meteo.com/v1/search"
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
        st.write("CURRENT WEATHER:")
        
        st.write(f"Temperature: {current["temperature_2m"]}℃")
        st.write(f"Humidity: {current["relative_humidity_2m"]}%")
        st.write(f"Wind speed: {current["wind_speed_10m"]}km/h")
        
        #modifying the WMO to english(alphabet)
        if weather_code == 0:
            st.write("Condition: Clear Sky ")
        elif weather_code == 1 or weather_code == 2 or weather_code == 3:
            st.write("Condition: Mainly clear, Partly cloudy, and Overcast ⛅")
        elif weather_code == 45 or weather_code == 48:
            st.write("Condition: fog and depositing rime fog 😶‍🌫️")
        elif weather_code == 51 or weather_code == 53 or weather_code == 55:
            st.write("Condition: Drizzle ")
        elif weather_code == 56 or weather_code == 57:
            st.write("Condition: Freezing Drizzle 🥶")
        elif weather_code == 61 or weather_code == 63 or weather_code == 65 or weather_code == 66 or weather_code == 67 or weather_code == 80 or weather_code == 81 or weather_code == 82: 
            st.write("Condition: Raining  🌧️")
        elif weather_code == 71 or weather_code == 73 or weather_code == 75 or weather_code == 77 or weather_code == 85 or weather_code == 86:
            st.write("Condition: Snow fall ❄️")

       # print()
        #print(f"{user_name}, thanks for using my weather forecast 😎❤️")

    except KeyError:
        st.write("PLEASE FILL THE FORM")
        print("you haven't entered the country you want to search for")
#thanks for using this. JOSHUA ISHAYA MUSA

 