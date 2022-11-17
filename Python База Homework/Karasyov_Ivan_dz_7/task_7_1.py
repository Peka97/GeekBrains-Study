import os

dirs_lst = ('settings', 'mainapp', 'adminapp', 'authapp')
for dir_name in dirs_lst:
	dir_path = os.path.join('my_project', dir_name)
	if not os.path.exists(dir_path):
		os.makedirs(dir_path)
