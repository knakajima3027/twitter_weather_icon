"""GET_weather.py"""
import json
import requests

def get_weather():
    key = 'e5ed5cd0f7ad46fb5413be93d4820565'
    url = 'http://api.openweathermap.org/data/2.5/weather?id=1850147&units=metric&appid' #東京都の現在の天気を取得

    return requests.get(url + '=' + key)

if __name__ == "__main__":
    get_weather()
