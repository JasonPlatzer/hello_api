import logging
import requests
import os




key = os.environ.get('WEATHER_KEY')


url = f'http://api.openweathermap.org/data/2.5/forecast'

def main():
    #from https://www.datadoghq.com/blog/python-logging-best-practices/
    logging.basicConfig(level=logging.DEBUG, filename='lab7_log.log', format='%(asctime)s %(levelname)s:%(message)s')
    location = get_location()
    # puts the results of get_current_weather into variables
    weather_data, error = get_current_weather(location, key)
    # if there is an exception raised in get_current_weather
    if error:
        logging.error(f'sorry cant get weather {weather_data}, {error}')
    else:
            # gets all the info in a list
            current_temp = get_temp(weather_data)
            # turns all the results into strings to be able to print them all
            for temp in current_temp:
                temp[0] = str(temp[0])
                temp[1] = str(temp[1])
                temp[2] = str(temp[2])
                temp[3] = str(temp[3])
                # displays all info
                print('At the time ' + temp[0] + ', the temp will be ' + 
                temp[1]+ 'C, the  outlook will be ' + temp[2] + ', the windspeed will be ' + 
                temp[3] + 'km/h.')
                
                    
            


def get_location():
    city, country = '',''
    while len(city)  == 0:
        city = input('enter city name: ')
        # if length of country is not equal to 2 or is not all letters
    while len(country) != 2 or not country.isalpha():
        country = input('enter 2 digit country code ' ).strip()
    # a string to use to query    
    Location = f'{city},{country}'
    logging.info(f'user has entered data {city}, {country}')
    return Location

def get_current_weather(location, key):
    try: 
        # what to query from database using location
        query = {'q': location,'units': 'metric', 'appid': key}
        # the query request the url + the the specific info the user wants to search for
        response = requests.get(url, params=query)
        # checking to see if there is an error
        response.raise_for_status()
        data = response.json() 
        # returns none if there is no exception
        return data, None
    except Exception as ex:
        logging.exception(f' error has occered {ex}')
        print(response.text)
        # returns no results of query and the exception
        return None, ex

def get_temp(weather_data):
    # a list for all the info
    five_days = []
    try:
        # 40 8 times a day the weather is posted times 5 days
        for i in range(40):
            # getting all the info and storing it in a list
            timestamp = weather_data['list'][i]['dt_txt']
            temp = weather_data['list'][i]['main']['temp']
            outlook = weather_data['list'][i]['weather'][0]['description']
            wind_speed = weather_data['list'][i]['wind']['speed']
            five_days.append([timestamp,temp,outlook, wind_speed])
            i += 1
               
        return five_days
    except KeyError as e:
        logging.exception(f' not json {e}')
        return 'Unknown'

if __name__ == '__main__':
    main()


# questions:
# 2. I will show time in utc time because that is easier for the user to figure out
# what time it is in their timezone
# 3. you should use print when you want to display something for the user you should
# use logging if it's data you want to see but you don't neccesarily want the user to see.
#
# you should not log sensitve information because other people could possibly be able to see it.  
