import os

folder = r'C:\Users\peka97\Desktop\GitHub\GB\Karasyov_Ivan_dz_7\some_data'
reply = [[0, set()], [0, set()], [0, set()], [0, set()]]  # Создал матрицу для упрощения сбора данных
for root, _, files in os.walk(folder):
	lst_extensions = []
	for file in files:
		file_extensions = file.split('.')[-1]
		os.chdir(root)
		size = os.stat(file).st_size
		if size < 100:
			reply[0][0] += 1
			if file_extensions not in reply[0][1]:
				reply[0][1].add(file_extensions)
		elif 100 < size < 1000:
			reply[1][0] += 1
			if file_extensions not in reply[1][1]:
				reply[1][1].add(file_extensions)
		elif 1000 < size < 10000:
			reply[2][0] += 1
			if file_extensions not in reply[2][1]:
				reply[2][1].add(file_extensions)
		elif size > 10000:
			reply[3][0] += 1
			if file_extensions not in reply[3][1]:
				reply[3][1].add(file_extensions)
		os.chdir(folder)

result, start, x = {}, 100, 0  # Преобразую матрицу в словарь
for _ in range(4):
	result[start] = reply[x][1]
	start *= 10
	x += 1

with open(f'{folder}_summary.json', 'w', encoding='utf-8') as f:  # Сохраняю данные
	f.write('{')
	for key, val in result.items():
		f.write(f'{key}: {val}, ')
	f.write('}')

with open(f'{folder}_summary.json', 'r', encoding='utf-8') as f:
	print(f.read())
