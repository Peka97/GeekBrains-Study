import requests as r
# from decimal import Decimal
from datetime import datetime
import utils

response = r.get("https://www.cbr.ru/scripts/XML_daily.asp")
parse_list = []


def get_values():
    for txt in response.text.split():
        if txt.startswith("Date"):
            date = txt.strip('"Date"= "').split('.')
            date_new = datetime(year=int(date[2]), month=int(date[1]), day=int(date[0])).date()
            print(date_new)
            print(type(date_new))  # Проверка класса
    for txt in response.text.split("<CharCode>"):
        for val in txt.split("<Value>"):
            parse_list.append(val.split("<")[0])
    del parse_list[0]


if __name__ == '__main__':
    get_values()
    print(*utils.currency_rates("EUR", parse_list))
    print(*utils.currency_rates("USD", parse_list))
