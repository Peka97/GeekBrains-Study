import os


MAIN_DIR = r'my_project'

root_dir = r'C:\Users\peka97\Desktop\GitHub\GB\Karasyov_Ivan_dz_7\my_project'
temp_dir = r'C:\Users\peka97\Desktop\GitHub\GB\Karasyov_Ivan_dz_7\templates'
if not os.path.exists(temp_dir):
	os.mkdir(temp_dir)
for root, dirs, files in os.walk(root_dir):
	for file in files:
		if file.endswith('.html'):
			cursor = 0
			for idx, item in enumerate(root.split("\\")):
				if item == 'templates':
					cursor = idx-1
			dir_name_for_temp = root.split("\\")[cursor]
			os.chdir(temp_dir)
			if not os.path.exists(dir_name_for_temp):
				os.makedirs(dir_name_for_temp)
			new_path = rf"{temp_dir}\{dir_name_for_temp}"
			os.chdir(new_path)
			with open(file, 'w') as f:
				print(f'Файл {file} создан в {new_path}')
