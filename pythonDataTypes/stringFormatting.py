print('Welcome {} {}'.format('hrishabkumar', 'jha'))

print('You are awesome {2} {1} {0}'.format('first','second','third'))

print('Number {t} {s} {f}'.format(f='first',s='second',t='third'))

#Float Formatting

result = 10/3

print('The result without precision {r}'.format(r=result))

print('The result with precision is {r:1.3f}'.format(r=result))


#f-sting method

print(f'The result using fstring method {result}')

name='hrishab'
age=25
print(f'{name} is {age} years old.')