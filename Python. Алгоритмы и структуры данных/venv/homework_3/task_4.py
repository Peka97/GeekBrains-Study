import hashlib
from uuid import uuid4


class Cash:
    def __init__(self) -> None:
        self.data = {}
        self.salt = uuid4().hex

    def get_values(self) -> dict:
        return self.data

    def check_url_hash(self, url) -> str | None:
        result = hashlib.sha256(self.salt.encode() + url.encode()).hexdigest()
        if self.data.get(url) == result:
            return result
        self.data[url] = result


if __name__ == '__main__':
    cash = Cash()
    print(cash.check_url_hash('https://vk.com/'))  # -> Не находит кэш и добавляет
    print(cash.check_url_hash('https://vk.com/'))  # -> Находит и выводит хэш в консоль
    print(cash.get_values())
