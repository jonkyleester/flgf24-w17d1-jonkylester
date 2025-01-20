import requests
import pandas as pd
from datetime import datetime, timedelta

API_KEY = 'your_api_key' 
base_url = 'https://api.weatherapi.com/v1/history.json'

# Defines the date range for the last 6 months
end_date = datetime.now()
start_date = end_date - timedelta(days=180)  # Approximately 6 months

# Creates an empty list to store the weather data
weather_data = []

# Iterates through the date range
for date in pd.date_range(start=start_date, end=end_date):
    params = {
        'key': '973efa14354146bf91f160018251901',
        'q': 'New York, NY',  
        'dt': date.strftime('%Y-%m-%d')  # Formats date for API
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        weather_info = {
            'date': data['forecast']['forecastday'][0]['date'],
            'avg_temp': data['forecast']['forecastday'][0]['day']['avgtemp_c'],
            'condition': data['forecast']['forecastday'][0]['day']['condition']['text']
        }
        weather_data.append(weather_info)
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Creates a pandas DataFrame from the collected data
df = pd.DataFrame(weather_data)

print(df)