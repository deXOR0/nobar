import os

cwd = '"' + os.getcwd() + '"'

os.system(f'cmd /c start chrome {cwd}\\nobar.html --allow-file-access-from-files')
os.system(f'cmd /k python {cwd}\\MoviePicker\\service.py')