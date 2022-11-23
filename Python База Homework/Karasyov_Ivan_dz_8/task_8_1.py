import re

SAMPLE = re.compile(r'^[a-z]+@[a-z]+\.[a-z]+')
email_1 = r'someone@geekbrains.ru'
email_2 = r'someone@geekbrainsru'
sample = {'username': 'someone', 'domain': 'geekbrains.ru'}


def email_parse(email: str):
	if SAMPLE.match(email):
		print({'username': email.split('@')[0], 'domain': email.split('@')[1]})
	else:
		msg = f': wrong email: {email}'
		raise ValueError(msg)


email_parse(email_1)
email_parse(email_2)
