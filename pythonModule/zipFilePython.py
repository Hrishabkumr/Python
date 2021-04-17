import zipfile
import shutil
f = open('one_file.txt','w+')
f.write('ONE FILE')
f.close()

f = open('second_file.txt','w+')
f.write('Second file')
f.close()

print('---- Zipping the File -----')
comp_file = zipfile.ZipFile('compress_file.zip','w')
comp_file.write('one_file.txt', compress_type= zipfile.ZIP_DEFLATED)
comp_file.write('second_file.txt', compress_type= zipfile.ZIP_DEFLATED)
comp_file.close()
print('---- Compress File Created Successfully ----')


print('---- unZipping File ----')
zip_obj = zipfile.ZipFile('compress_file.zip','r')
zip_obj.extractall('ExtractedFolder')
zip_obj.close()
print('-----File UnZipped Successfully -----')

print('---- to Zip Entire Folder ----')
dir_to_zip = 'D:\EclipseWorkspace\PythonFirst\src\pythonModule\ExtractedFolder'
output_filename = 'example'
shutil.make_archive(output_filename, 'zip', dir_to_zip)
print('---- Zip Entire Folder Created successfully ----')

print('--- step to unpack archieve folder ---')
dir_to_unzip = 'D:\EclipseWorkspace\PythonFirst\src\pythonModule\extract'
shutil.unpack_archive('example.zip', dir_to_unzip)

