import math
import random

#print(help(math))

print(f'pi: {math.pi}')
print(f'e: {math.e}')
print(f'Math degrees {math.radians(30)}')
print(f'sin 30 : {math.sin(math.radians(30))}')
print(f'sin 60 : {math.sin(math.radians(60))}')
print(f'sin 90 : {math.sin(math.radians(90))}')
print(f'log : {math.log(math.e)}')

#random.seed(101)
print(f'Random : {random.randint(0,100)}')
print(f'Random : {random.randint(0,100)}')
print(f'Random : {random.randint(0,100)}')
print(f'Random : {random.randint(0,100)}')
print(f'Random : {random.randint(0,100)}')

mylist = list(range(0,20))
print(mylist)
print(f'Choice value : {random.choice(mylist)}')
print(f'Choice value : {random.choice(mylist)}')
print(f'Sample value with replacement : {random.choices(population=mylist,k=10)}')
print(f'Sample value without replacement : {random.sample(population=mylist,k=5)}')

random.shuffle(mylist)
print(f'Suffle list : {mylist}')

