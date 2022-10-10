from uuid import uuid4
import hashlib
import json
import sqlite3

salt = uuid4().hex
conn = sqlite3.connect('data.db')
conn.execute('''CREATE TABLE IF NOT EXISTS users (
    id SERIAL,
    password VARCHAR(255) NOT NULL);
    ''')
conn.commit()


def auth_with_json(pswd: str) -> None:
    pswd = hashlib.sha256(salt.encode() + pswd.encode()).hexdigest()
    with open('data.json', 'w+', encoding='utf-8') as file:
        json.dump({1: pswd}, file)
    print(f'В базе данных хранится строка: {pswd}')

    get_pswd = input('Введите пароль ещё раз для проверки: ')
    get_pswd = hashlib.sha256(salt.encode() + get_pswd.encode()).hexdigest()

    with open('data.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    if get_pswd in data.values():
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели неправильный пароль. Повторите попытку')


def auth_with_sql(pswd: str) -> None:
    pswd = hashlib.sha256(salt.encode() + pswd.encode()).hexdigest()
    conn.execute('''INSERT INTO users (id, password) 
                    VALUES (?, ?)''', (1, pswd))
    conn.commit()

    get_pswd = input('Введите пароль ещё раз для проверки: ')
    get_pswd = hashlib.sha256(salt.encode() + get_pswd.encode()).hexdigest()

    data = conn.execute(f'SELECT password FROM users').fetchall()
    if (get_pswd,) in data:
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели неправильный пароль. Повторите попытку')


if __name__ == '__main__':
    password = input('Введите пароль: ')
    auth_with_json(password)  # Вариант с json
    auth_with_sql(password)  # Вариант с sqllite
