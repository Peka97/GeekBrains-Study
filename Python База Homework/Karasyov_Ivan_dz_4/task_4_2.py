import requests as r
from decimal import Decimal

response = r.get("https://www.cbr.ru/scripts/XML_daily.asp")
parse_list = []


def get_values():
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
print(*currency_rates("USD"))
