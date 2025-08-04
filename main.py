import requests
from telegram_connect import SendMessage
from refresh_cookie import RefreshToken
import json
import time;import datetime

cookies = {
    "access_token_web": open("access_token.json").read()
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

url = "https://www.vinted.pl/api/v2/catalog/items"

config = open("config.json", encoding="utf8").read()
config = json.loads(config)

items_handled = []
print("["+datetime.datetime.now().strftime('%d.%m.%Y %H:%M')+"] Uruchamianie aplikacji...")
while True:
    response = requests.get(url, headers=headers, params=config["params"], cookies=cookies)
    if response.status_code == 403:
        print("["+datetime.datetime.now().strftime('%d.%m.%Y %H:%M')+"] Błąd tokenu, odświeżam...")
        RefreshToken(url="https://www.vinted.pl/")
        time.sleep(5)
    else:
        try:
            for rekord in response.json()["items"]:
                if (rekord["id"] not in items_handled):
                    items_handled.append(rekord["id"])
                    if len(items_handled) > 50:
                        items_handled.pop(0)
                    SendMessage(config["telegram"]["token"], config["telegram"]["chat_id"], "Wykryto nowe ogłoszenie <a href='https://vinted.pl" + rekord["path"] + "'>" + rekord["item_box"]["first_line"] + "</a> za " + rekord["price"]["amount"] + " " + rekord["price"]["currency_code"] )
                    print("["+datetime.datetime.now().strftime('%d.%m.%Y %H:%M')+"] Wysłano do "+ str(config['telegram']['chat_id'])+" ogłoszenie o ID "+str(rekord['id']))
                else:
                    pass
            
        except Exception:
            pass
        time.sleep(5)
