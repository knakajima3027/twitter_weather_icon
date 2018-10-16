"""GET_weather.py"""
import json
import requests

def get_weather():
    key = 'your open weathermap api key'
    url = 'http://api.openweathermap.org/data/2.5/weather?id=1850147&units=metric&appid' #東京都の現在の天気を取得
    j_file = requests.get(url + '=' + key)
    j_file = j_file.json()

    return j_file['weather'][0]['description']

def get_icon():
    weather = get_weather()
    
    if weather == 'clear sky':
        icon = '🌞'

    elif weather == 'few clouds':
        icon = '🌤'

    elif weather == 'scattered clouds':
        icon = '⛅'

    elif weather == 'broken clouds':
        icon = '☁'

    elif weather == 'shower rain':
        icon = '☂'

    elif weather == 'rain':
        icon = '☔'

    elif weather == 'thunderstorm':
        icon = '⚡'

    elif weather == 'snow':
        icon = '☃'

    elif weather == 'mist':
        icon = '🌂'

    else:
        icon = '❓'

    return icon

if __name__ == "__main__":
    print(get_icon())
