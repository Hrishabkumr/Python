myFile = open('myFile.txt')
print(myFile.read())
myFile.seek(0)
print(myFile.read())
myFile.seek(0)

print(myFile.readlines())

myFile.close()

with open('myFile.txt') as my_new_file:
    contents = my_new_file.read()

print(contents)


#mode example
print("-------Mode example--------")
with open('myNewFile.txt',mode='r') as f:
    print(f.read())

with open('myNewfile.txt',mode='a') as f:
    f.write('\nFour on Fourth')

with open('myNewFile.txt',mode='r') as f:
    print(f.read())

print("-------Mode example w (overwrite the file or create the new file)--------")
with open('createnewFiletext.txt',mode='w') as f:
    f.write('This is new line in the new file!!!Woohoo')
    
myfile = open('createnewFiletext.txt')
print(myfile.read())
myfile.close()