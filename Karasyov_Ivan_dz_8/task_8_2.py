import re

RE_remote_addr = re.compile(r'^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+')
RE_request_datetime = re.compile(r'[0-9]{2}/[A-Za-z]+/[0-9]{4}:[0-9]{2}:[0-9]{2}:[0-9]{2}\s\+[0-9]{4}')
RE_request_type = re.compile(r'"[A-Z]{3}')
RE_requested_resource = re.compile(r'/[a-z]+/[a-z0-9]+')
RE_response_code = re.compile(r'\s([1-6]{3}|\d0\d)\s')
RE_response_size = re.compile(r'\s(\d[1-9]\d+|[0-9]|[3-5]00|\d{4,})\s')
extemptions = []
# Не вошло буквально 8 примеров, у которых code и size, например, 404 и 304. Тут уже шаблон подгонять сложно.
# Разве что парсить кусок в code и size и делить его по пробелу. Исключения занесу в список


def is_valid(text):
	reply = []
	temps = [RE_remote_addr, RE_request_datetime, RE_request_type, RE_requested_resource, RE_response_code, RE_response_size]
	for temp in temps:
		if re.search(temp, text):
			reply.append(re.search(temp, text).group())
		else:
			extemptions.append(f"   Шаблон: {temp}\n    Текст:{text}")
			break
	if len(reply) == len(temps):
		print(tuple(reply))
	del reply


with open("nginx_logs.txt", "r", encoding='utf-8') as file:
	for line in file.readlines():
		is_valid(line)
	for el in extemptions:
		print(f"\nИсключениe:\n{el}")
	print(f"Кол-во исключений: {len(extemptions)}")
