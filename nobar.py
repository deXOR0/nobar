import os
from sys import platform

cwd = '"' + os.getcwd() + '"'

def error(msg):
	print(f'[ERROR] {msg}')

if platform == 'linux' or platform == 'linux2' or platform == 'darwin':
	os.system(f'google-chrome {cwd}/nobar.html --allow-file-access-from-files & python3 {cwd}/MoviePicker/service.py')
elif platform == 'win32' or platform == 'win64':
	os.system(f'cmd /c start chrome {cwd}\\nobar.html --allow-file-access-from-files')
	os.system(f'cmd /k python {cwd}\\MoviePicker\\service.py')
else:
	error('OS is not supported!')
