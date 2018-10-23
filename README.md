## できること  
twitterの名前欄に東京の天気に対応したアイコンを付与できます．  
参考:https://qiita.com/issei_y/items/ab641746be2704db98be  

## 1. Twitter developer acount の申請 (APIを利用するため)
https://developer.twitter.com  
取得した値を`aws_function/config.py`の各値に入力  
## 2. OpenWeatherMap のアカウント作成 (APIを利用するため)
https://home.openweathermap.org/users/sign_up  
取得した値を`aws_function/GET_Weather.py`のkeyに入力
## 3. AWSのLumbdaにアップロード  
https://aws.amazon.com/jp/lambda/  
この`aws_function`をzipに圧縮`zip -r aws_function`して，Lumbdaのコードエントリーにアップロード
