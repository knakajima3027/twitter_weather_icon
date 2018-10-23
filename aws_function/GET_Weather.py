"""get_weather.py"""
import json
import requests
from datetime import datetime
from datetime import timedelta

'''openweatherから受けとったjsonファイルから日の出の時刻, 日没の時刻, 現在の天気を取得して返す'''
def get_weather():
    key = 'your open weathermap api key' #ここにapiキーを入力
    url = 'http://api.openweathermap.org/data/2.5/weather?id=1850147&units=metric&appid' #東京都の現在の天気を取得
    j_file = requests.get(url + '=' + key)
    j_file = j_file.json()

    weather = j_file['weather'][0]['id']
    sun_rise = datetime.fromtimestamp(j_file['sys']['sunrise']) #日の出時間を取得
    sun_set = datetime.fromtimestamp(j_file['sys']['sunset']) #日の入り時間を取得

    return weather, sun_rise, sun_set

'''時間, 天気に対応したアイコンを返す'''
def get_icon():
    now = datetime.now() #現在の時間を取得
    weather, sun_rise, sun_set = get_weather()

    if weather in range(200, 233):
        icon = '⚡'

    elif weather in range(300, 322):
        icon = '🌂'

    elif weather in range(500, 532):  #雨
        icon = '☔'

    elif weather in range(600, 623):
        icon = '☃'

    elif weather in range(701, 782):
        if sun_rise <= now < sun_rise + timedelta(minutes = 30): #日の出から1時間
            icon = '🌄'
        elif sun_rise + timedelta(minutes = 30) <= now < sun_set:#日中
            icon = '🌫'
        elif sun_set <= now <= sun_set + timedelta(minutes = 30): #日の入りから一時間
            icon = '🌇'
        else:                                               # 夜
            icon = '🌟'

    elif weather == 800:
        if sun_rise <= now < sun_rise + timedelta(minutes = 30): #日の出から1時間
            icon = '🌄'
        elif sun_rise + timedelta(minutes = 30) <= now < sun_set: #日中
            icon = '☀'
        elif sun_set <= now <= sun_set + timedelta(minutes = 30): #日の入りから一時間
            icon = '🌇'
        else:                                                # 夜
            icon = '🌟'

    elif weather == 801:
        if sun_rise <= now < sun_rise + timedelta(minutes = 30): #日の出から1時間
            icon = '🌄'
        elif sun_rise + timedelta(minutes = 30) <= now < sun_set: #日中
            icon = '🌤'
        elif sun_set <= now <= sun_set + timedelta(minutes = 30): #日の入りから一時間
            icon = '🌇'
        else:                                               # 夜
            icon = '🌟'

    elif weather == 802:
        if sun_rise <= now < sun_rise + timedelta(minutes = 30): #日の出から1時間
            icon = '🌄'
        elif sun_rise + timedelta(minutes = 30) <= now < sun_set:#日中
            icon = '🌥'
        elif sun_set <= now <= sun_set + timedelta(minutes = 30): #日の入りから一時間
            icon = '🌇'
        else:                                               # 夜
            icon = '🌟'

    elif weather in (803, 804):
        if sun_rise <= now < sun_rise + timedelta(minutes = 30): #日の出から1時間
            icon = '🌄'
        elif sun_rise + timedelta(minutes = 30) <= now < sun_set:#日中
            icon = '☁'
        elif sun_set <= now <= sun_set + timedelta(minutes = 30): #日の入りから一時間
            icon = '🌇'
        else:                                               # 夜
            icon = '🌟'

    else:
        icon = '❓'

    return icon
