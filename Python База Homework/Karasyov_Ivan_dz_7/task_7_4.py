import os

folder = r'C:\Users\peka97\Desktop\GitHub\GB\Karasyov_Ivan_dz_7\some_data'
result = {}
start = 100
for _ in range(4):
	result[start] = 0
	start *= 10
for root, _, files in os.walk(folder):
	for file in files:
		os.chdir(root)
		size = os.stat(file).st_size
		if size < 100:
			result[100] += 1
		elif 100 < size < 1000:
			result[1000] += 1
		elif 1000 < size < 10000:
			result[10000] += 1
		elif size > 10000:
			result[100000] += 1
		os.chdir(folder)

print(result)
