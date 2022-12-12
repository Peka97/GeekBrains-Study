def data_users_v2():
	result = []
	with open('users.csv', 'r', encoding='utf-8') as users:
		with open('hobby.csv', 'r', encoding='utf-8') as hobby:
			user_next = users.readline().strip('\n').replace(',', ' ')
			hobby_next = hobby.readline().strip('\n').replace(',', ' ')
			while user_next or hobby_next:
				if len(user_next) > 0 and len(hobby_next) == 0:
					hobby_next = "None"
					result.append(f"{user_next}: {hobby_next}")
				elif len(user_next) == 0 and len(hobby_next) >= 0:
					print(1)
					break
				else:
					result.append(f"{user_next}: {hobby_next}")
				user_next = users.readline().strip('\n').replace(',', ' ')
				hobby_next = hobby.readline().strip('\n').replace(',', ' ')
	with open('users_hobby.txt', 'w+', encoding='utf-8') as result_file:
		for item in result:
			result_file.write(f"{item}\n")
	with open('users_hobby.txt', 'r', encoding='utf-8') as result_file:
		print(result_file.read())


data_users_v2()
