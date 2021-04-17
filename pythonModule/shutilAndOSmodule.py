import os
import shutil
print(os.getcwd())

print(os.listdir())

print(os.listdir('D:\EclipseWorkspace\PythonFirst'))

#shutil.move('D:\EclipseWorkspace\PythonFirst\src\FirstModule.py','D:\EclipseWorkspace\PythonFirst\src\pythonModule')

print(os.cpu_count())

file_path = 'D:\EclipseWorkspace\PythonFirst\src'
for folder,sub_folder,files in os.walk(file_path):
    
    print(f'Currently inside folder {folder}')
    print('\n')

    for sub_fold in sub_folder:
        print(f'Subfolder: {sub_fold}')
    
    print('\n')
    print('The Files are: ')
    for f in files:
        print(f'\t File : {f}')