from random import shuffle
x = [1,2,3,4,5]

for num in range(1,10,2):
    print(num)
    
word = 'welcome to world'
for letter in word:
    print(letter)

print('----Use of Enumerate----')
for index,letter in enumerate(word):
    print(index)
    print(letter)

print('------Use of Zip------return tuple')
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
for item in zip(mylist1,mylist2,mylist3):
    print(item)

print('-----Print Zip result------')
ziplist = list(zip(mylist1,mylist2,mylist3))
print(ziplist)

print('-----use of in to check data present or not-----')
print('x' in ['1','2','3'])
print(1 in [1,'2','3'])
print('1' in [1,'2','3'])

print('----Result using shuffle-----')

mylist = [1,2,3,4,5,6,7,8]
shuffle(mylist)
print(f'Shuffle result {mylist}')
print(f'min value from list {min(mylist)}')
print(f'max value from list {max(mylist)}')

print('----Result using randint-----')
from random import randint
mynum = randint(0,10)
print(f'Random number {mynum}')

print('----use of Input ----a')
result = input('What is your name?')
print(f'Name :{result}')

result = input('What is your name?')
print(f'Name :{result}')



