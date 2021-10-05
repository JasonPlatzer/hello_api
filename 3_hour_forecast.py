from pprint import pprint
import requests
import os
from datetime import datetime

key = os.environ.get('WEATHER_KEY')
#http://api.openweathermap.org/data/2.5/forecast?q=minneapolis,us&units=imperial&id={key}

query = {'q': 'minneapolis,us', 'units': 'imperial', 'appid': key}
url = 'http://api.openweathermap.org/data/2.5/forecast'
data = requests.get(url, params=query).json()
#pprint(data)
list_of_forecasts = data['list']
for forecast in list_of_forecasts:
    temp = forecast['main']['temp']
    timestamp = forecast['dt']
    forecast_date = datetime.fromtimestamp(timestamp)
    print(f' at {forecast_date} the temp will be {temp}F')
