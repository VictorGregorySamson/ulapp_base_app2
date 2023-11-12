from flask import Flask
import requests
import json

#Create Flask application
Ulapp = Flask(__name__) 

# API of open weather app
API_KEY = 'c3ab9a2a4ccfaac2065c44ce3977630b'

def get_5_day_forecast(city_name):
    base_url = 'http://api.openweathermap.org/data/2.5/forecast'
    
    # Parameters na nagbibigay ng Pighati
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric',  #
    }
    
    # Request data (mapapadpad nako sa psychward)
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None

@Ulapp.route('/display_weather_forecast/<city_name>')
def display_5_day_forecast(data):
    if data:
        city = data['city']['name']
        forecast_list = data['list']

        print(f"5-Day Weather Forecast for {city}:\n")

        # Keeps track of the days and adds 1 if the next day is outputted 
        current_day = None
        day_counter = 0

        for item in forecast_list:
            timestamp = item['dt_txt']
            date = timestamp.split()[0]  # Extract date from the api

            # Here comes the sun do ro do ro (Checker for a new day in the forecast)
            if date != current_day:
                current_day = date
                if day_counter < 5:  # Display only 5 days
                    day_counter += 1
                    print(f"Day {day_counter}:")
                else:
                    break

            temperature = item['main']['temp'] # Hot or Cold? Palibre
            description = item['weather'][0]['description'] # Cloudy with a chance of meatballs
            humidity = item['main']['humidity'] # Water vapor in the atmosphere
            wind_speed = item['wind']['speed'] # Ang lameg ng  hangin payakap naman          
            rain_3h = item.get('rain', {}).get('3h', 0) # Gets the depth of rain from the last 3 hrs. So 1 mm of rain translates to 1 litre of water in a single metre square (Sabi ni Google lmao)

            return "Hello"
            print(f"Date & Time: {timestamp}")
            print(f"Temperature: {temperature}°C")
            print(f"Description: {description}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} m/s")
            print(f"Rain (3h): {rain_3h} mm\n")

    else:
        print("No data found :(")

if __name__ == '__main__':
    Ulapp.run()
    print('Ulapp Forecasting(BETA)')
    city_name = input("Enter city name: ")
    forecast_data = get_5_day_forecast(city_name)
    display_5_day_forecast(forecast_data)
