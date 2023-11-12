import requests
import json

# API Key
API_KEY = 'c3ab9a2a4ccfaac2065c44ce3977630b'

def get_weather(city_name):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    
    # Parameters na nagbibigay ng Pighati
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric',
    }
    
    # Request data
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: {response.status_code}")
        return None

def display_weather_data(data):
    if data:
        city = data['name']
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        
        #Rain data (Umuulan mata ko sa code na to)
        if 'rain' in data:
            rain = data['rain']
            if '1h' in rain:
                chance_of_rain = f"Chance of rain: {rain['1h']} mm in the last hour"
            else:
                chance_of_rain = "No recent rain data available"
        else:
            chance_of_rain = "No rain data available"

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Description: {description}")  
        print(f"Humidity: {humidity}%")
        print(chance_of_rain)
    else:
        print("No data available")

if __name__ == '__main__':
    city_name = input("Enter city name: ")
    weather_data = get_weather(city_name)
    display_weather_data(weather_data)
