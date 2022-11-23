import os

if os.path.exists('my_project'):
	print("Вижу существующую папку my_project. Удали её, иначе код не будет работать")
else:
	with open('config.yaml', encoding='utf-8') as file:
		main_dir = ""
		sub_dir = ""
		sub2_dir = ""
		sub3_dir = ""
		for line in file.readlines():
			os.chdir(r'C:\Users\peka97\Desktop\GitHub\GB\Karasyov_Ivan_dz_7')
			structure = line.strip("\t\n ").split(':')
			directory = structure[0]
			files = str(line.strip("\t\n ").split(':')[1:]).strip("[']").split(',')
			if directory[3] == '$' and not os.path.exists(directory.strip('$')):
				sub3_dir = directory.strip('$')
				dir_name = f"{main_dir}/{sub_dir}/{sub2_dir}/"
				dir_path = os.path.join(dir_name, directory.strip('$'))
				os.makedirs(dir_path)
				os.chdir(dir_path)
				for file_name in files:
					with open(file_name.strip(), 'w') as f:
						f.close()
			elif directory[2] == '$' and not os.path.exists(directory.strip('$')):
				sub2_dir = directory.strip('$')
				dir_name = f"{main_dir}/{sub_dir}"
				dir_path = os.path.join(dir_name, directory.strip('$'))
				os.makedirs(dir_path)
				os.chdir(dir_path)
				for file_name in files:
					if file_name != '':
						with open(file_name.strip(), 'w') as f:
							f.close()
			elif directory[1] == '$' and not os.path.exists(directory.strip('$')):
				sub_dir = directory.strip('$')
				dir_name = main_dir
				dir_path = os.path.join(dir_name, directory.strip('$'))
				os.makedirs(dir_path)
				os.chdir(dir_path)
				for file_name in files:
					with open(file_name.strip(), 'w') as f:
						f.close()
			elif directory[0] == '$' and not os.path.exists(directory.strip('$')):
					main_dir = directory.strip('$')
					os.mkdir(main_dir)
