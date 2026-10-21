import requests
from datetime import date

URL = "https://www.cbr-xml-daily.ru/daily_json.js"
valutes = ['USD', 'EUR', 'CNY']

try:
    answer = requests.get(URL, timeout=10)
    answer.raise_for_status()
    data = answer.json()

    with open('prices.txt', 'a', encoding='utf-8') as f:
        for code in valutes:
            value = data["Valute"][code]["Value"]
            line = f"{date.today()} {code} -> {value}"
            print(line)
            f.write(line + "\n")

except requests.exceptions.RequestException as e:
    print(f"Не удалось получить данные: {e}")
except KeyError as e:
    print(f"В ответе нет нужной валюты или поля: {e}")
    