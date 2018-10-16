import json, config
from requests_oauthlib import OAuth1Session
from GET_Weather import get_icon
"""認証関連"""
CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS)

weather_icon = get_icon() #天気の取得&天気アイコンの取得

"""プロフィール, 名前の変更"""
url = 'https://api.twitter.com/1.1/account/update_profile.json'
method = 'POST'

params = {'name':'your twitter name' + weather_icon}
res = twitter.post(url, params = params)
