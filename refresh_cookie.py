import requests
import re
import datetime

def RefreshToken(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.35 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.35",
        "sec-ch-ua-platform": '"Windows"',
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9,pl-PL;q=0.8,pl;q=0.7",
        "Cache-Control": "max-age=0",
        "Referer": "https://www.google.com/",
        "Connection": "keep-alive",
        "Host": "www.vinted.pl",
    }

    response = requests.get(url, headers=headers)

    try:
        test = response.headers['Set-Cookie']
        match = re.search(r'access_token_web=([^;]+)', test)
        if match:
            token = match.group(1)
            with open("access_token.json", "w") as f:
                f.write(token)
        else:
            print("["+datetime.datetime.now().strftime('%d.%m.%Y %H:%M')+"] Błąd w generowaniu tokenu, nie wykryto access_token_web...")
    except Exception:
        pass
    return