from pprint import pprint
import requests
import os




key = os.environ.get('WEATHER_KEY')

#print(key)
#url = f'http://api.openweathermap.org/data/2.5/weather'
#url = f'http://api.openweathermap.org/data/2.5/weather?q=minneapolis,mn,us&units=imperial&appid={key}'
# dont use f-strings
#query = {'q': 'tokyo,jp', 'units': 'imperial', 'appid': key}
#data = requests.get(url).json()
#data = requests.get(url, params=query).json()
#pprint(data)
#temp = data['main']['temp']
#print(f'The current temperature is {temp} %F')

#city = input('what city would you like to see ')
#state = input('if in us what state is it in or press enter if not is us ')
#country = input('what country code is it ' )
#url = f'http://api.openweathermap.org/data/2.5/weather?q={city},{state,}{country},us&units=imperial&appid={key}'
#data = requests.get(url).json()
#temp = data['main']['temp']
#print(f'The current temperature is {temp} %F')
#url = f'http://api.openweathermap.org/data/2.5/weather'
#location = f'{city},{country}'
#query = {'q': location, 'appid': key }
#data = requests.get(url, params=query).json()



url = f'http://api.openweathermap.org/data/2.5/weather'

def main():
    location = get_location()
    weather_data, error = get_current_weather(location, key)
    if error:
        print('sorrty cant get weather')
    else:
        current_temp = get_temp(weather_data)
        print(f' the currect temp is {current_temp}C')


def get_location():
    city, country = '',''
    while len(city)  == 0:
        city = input('enter city name: ')
    while len(country) != 2 or not country.isalpha():
        country = input('enter 2 digit country code' ).strip()
    Location = f'{city},{country}'
    return Location

def get_current_weather(location, key):
    try: 
        query = {'q': location, 'units': 'metric', 'appid': key}
        response = requests.get(url, params=query)
        response.raise_for_status()
        data = response.json() #may errorr too if not json
    
        return data, None
        # returns a tuple
    except Exception as ex:
        print(ex)
        print(response.text)
        return None, ex

def get_temp(weather_data):
    try:
        temp = weather_data['main']['temp']
        return temp
    except KeyError:
        print(' not json')
        return 'Unknown'

if __name__ == '__main__':
    main()

#http://api.openweathermap.org/data/2.5/forecast?q=minneapolis,us&units=imperial&id={key}