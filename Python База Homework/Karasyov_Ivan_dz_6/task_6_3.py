def data_users():
	result = {}
	with open('users.csv', 'r', encoding='utf-8') as users:
		with open('hobby.csv', 'r', encoding='utf-8') as hobby:
			for _ in range(3):
				result[users.readline().strip('\n').replace(',', ' ')] = hobby.readline().strip('\n').replace(',', ', ')
	with open('result.csv', 'w+', encoding='utf-8') as result_file:
		for key, val in result.items():
			if len(key) > 0 and len(val) == 0:
				val = "None"
				result_file.writelines(f"{key}: {val},\n")
			elif len(key) == 0 and len(val) >= 0:
				print(1)
				break
			else:
				result_file.writelines(f"{key}: {val},\n")


data_users()
with open('result.csv', 'r', encoding='utf-8') as file:
	print(file.read())
