import time
import requests
from bs4 import BeautifulSoup
import json, config #標準のjsonモジュールとconfig.pyの読み込み
from requests_oauthlib import OAuth1Session #OAuthのライブラリの読み込み
import urllib.parse

CK = config.CONSUMER_KEY
CS = config.CONSUMER_SECRET
AT = config.ACCESS_TOKEN
ATS = config.ACCESS_TOKEN_SECRET
twitter = OAuth1Session(CK, CS, AT, ATS) #認証処理



url = "https://api.twitter.com/1.1/statuses/update.json" #ツイートポストエンドポイント

# print("内容を入力してください。")
# tweet = input('>> ') #キーボード入力の取得
# print('*******************************************')

tweet = 'テストきええええええええ！！'

params = {"status" : tweet}

res = twitter.post(url, params = params) #post送信

if res.status_code == 200: #正常投稿出来た場合
    print("Success.")
else: #正常投稿出来なかった場合
    print("Failed. : %d"% res.status_code)
    print(res)


try:
    # urlを代入
    url = "https://www.amazon.co.jp/Nintendo-Switch-%E3%83%8B%E3%83%B3%E3%83%86%E3%83%B3%E3%83%89%E3%83%BC%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81-%E3%83%8D%E3%82%AA%E3%83%B3%E3%83%AC%E3%83%83%E3%83%89%E3%80%91-%E3%83%8B%E3%83%B3%E3%83%86%E3%83%B3%E3%83%89%E3%83%BCe%E3%82%B7%E3%83%A7%E3%83%83%E3%83%97%E3%81%A7%E3%81%A4%E3%81%8B%E3%81%88%E3%82%8B%E3%83%8B%E3%83%B3%E3%83%86%E3%83%B3%E3%83%89%E3%83%BC%E3%83%97%E3%83%AA%E3%83%9A%E3%82%A4%E3%83%89%E7%95%AA%E5%8F%B73000%E5%86%86%E5%88%86/dp/B07SVXHD1P/ref=sr_1_15?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&dchild=1&keywords=%E3%82%B9%E3%82%A4%E3%83%83%E3%83%81&qid=1593687638&sr=8-15"


    # 待機
    # time.sleep(5)
    # データ取得
    res = requests.get(url).text
    # 要素の抽出
    soup = BeautifulSoup(res, "html.parser")
    item = soup.find('input',id="add-to-cart-button")
    print (item['value'])
      


    # tags = soup.find_all("a")
    # # タグ内テキスト
    # for tag in tags:
    #     print(tag.get_text())
except:
    print("取得できませんでした")