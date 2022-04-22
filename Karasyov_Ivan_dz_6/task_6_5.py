import sys


def data_users_v3(argv):
	users_filename, hobby_filename, result_file_filename = argv
	result = []
	with open(f'{users_filename}', 'r', encoding='utf-8') as users:
		with open(f'{hobby_filename}', 'r', encoding='utf-8') as hobby:
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
	with open(f'{result_file_filename}', 'w+', encoding='utf-8') as result_file:
		for item in result:
			result_file.write(f"{item}\n")
	with open(f'{result_file_filename}', 'r', encoding='utf-8') as result_file:
		print(result_file.read())


if __name__ == '__main__':
	exit(data_users_v3(sys.argv))

