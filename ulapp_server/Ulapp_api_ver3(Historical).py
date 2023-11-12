import requests
import json
import pandas as pd
import os
from flask import Flask

# App instance
ulapp = Flask(__name__)

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
    
@ulapp.route('/test')
def get_forecast_for_api():
    return compiled_forecast_data

def display_5_day_forecast(data):
    compiled_forecast_data = {} # Dictionary for the compilation of weather of all the days

    if data:
        city = data['city']['name']
        forecast_list = data['list']

        # Keeps track of the days
        current_day = None
        day_counter = 0

        # Create an Excel writer with the specified filename
        save_directory = r"C:\Next.js\\"
        excel_filename = f"{save_directory}{city}_5_day_forecast.xlsx"

        with pd.ExcelWriter(excel_filename, engine='xlsxwriter') as writer:
            for index, item in enumerate(forecast_list):
                timestamp = item['dt_txt']
                date = timestamp.split()[0]  # Extract date from the API

                # Checker for a new day in the forecast
                if date != current_day:
                    if current_day is not None:
                        # Save the DataFrame to a new sheet
                        df = pd.DataFrame(forecast_data_to_save)
                        df.to_excel(writer, index=False, sheet_name=f'Day {current_day}')

                    current_day = date
                    day_counter += 1
                    print(f"Day {day_counter}:")
                    
                    # Empty list for excel file
                    forecast_data_to_save = [] 
                    # Empty dictionary to store data for the current day
                    forecast_data = {}

                day_data = {
                    'Date & Time': timestamp,
                    'Temperature (°C)': item['main']['temp'],
                    'Description': item['weather'][0]['description'],
                    'Humidity (%)': item['main']['humidity'],
                    'Wind Speed (m/s)': item['wind']['speed'],
                    'Rain (3h) (mm)': item.get('rain', {}).get('3h', 0)
                }

                forecast_data_to_save.append(day_data)
                forecast_data.update({f'timestamp {index + 1}' : day_data})
                compiled_forecast_data.update({f'Day {day_counter}'  :  forecast_data})

                print(f"Date & Time: {day_data['Date & Time']}")
                print(f"Temperature: {day_data['Temperature (°C)']}") # Hot or Cold? Palibre
                print(f"Description: {day_data['Description']}") # Cloudy with a chance of meatballs
                print(f"Humidity: {day_data['Humidity (%)']}") # Water vapor in the atmosphere
                print(f"Wind Speed: {day_data['Wind Speed (m/s)']}") # Ang lameg ng  hangin payakap naman  
                print(f"Rain (3h): {day_data['Rain (3h) (mm)']}\n") # Gets the depth of rain from the last 3 hrs. So 1 mm of rain translates to 1 litre of water in a single metre square (Sabi ni Google lmao)

            # Save the last day's data to a new sheet (Ang weird Kase, may ouptut sa side na saved to day 6)
            df = pd.DataFrame(forecast_data_to_save)
            df.to_excel(writer, index=False, sheet_name=f'Day {current_day}')

        save_to_excel = input("Do you want to save the 5-Day Weather Forecast to Excel? (yes/no): ").lower()

        if save_to_excel == 'yes':
            print(f"5-Day Weather Forecast saved to {excel_filename}")
        else:
            os.remove(excel_filename)
            print("Forecast data not saved.")
    else:
        print("No data found :(")

    return compiled_forecast_data

if __name__ == '__main__':
    print('Ulapp Forecasting(BETA)')
    city_name = input("Enter city name: ")
    forecast_data = get_5_day_forecast(city_name)
    compiled_forecast_data = display_5_day_forecast(forecast_data)
    ulapp.run(debug=True)