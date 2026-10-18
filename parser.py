import requests
from datetime import date

try:
    answer = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
except ValueError as e:
     print(e)

data = answer.json()
valutes = ['USD', 'EUR', 'CNY']

for i in valutes:
    valute = (f'{i} -> {data['Valute'][i]['Value']}')
    print(valute)
    with open('prices.txt', 'a', encoding='utf-8') as f:
        f.write(f'{date.today()} {valute} {'\n'}')