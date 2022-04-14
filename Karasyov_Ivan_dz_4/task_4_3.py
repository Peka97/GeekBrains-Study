import requests as r
# from decimal import Decimal
from datetime import datetime


response = r.get("https://www.cbr.ru/scripts/XML_daily.asp")
parse_list = []


def get_values():
    for txt in response.text.split():
        if txt.startswith("Date"):
            date = txt.strip('"Date"= "').split('.')
            date_new = datetime(year=int(date[2]), month=int(date[1]), day=int(date[0]))
            print(date_new)
            print(type(date_new))  # Проверка класса
    for txt in response.text.split("<CharCode>"):
        for val in txt.split("<Value>"):
            parse_list.append(val.split("<")[0])
    del parse_list[0]


def currency_rates(x):
    for idx, text in enumerate(parse_list):
        if text == x.lower() or text == x.upper():
            return text, parse_list[idx + 1]
    return None


get_values()
print(*currency_rates("EUR"))
print(*currency_rates("USD"))  # Выводил все в float с теми же величинами. Не очень понял зачем здесь Decimal
