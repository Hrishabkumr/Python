x = 1
while x<5:
    print('The current value of x is {}'.format(x))
    x = x+1
else:
    print('Reached 5')
    

x = [1,2,3]
for num in x:
    pass

print('out of for loop')

name = 'hrishabkumar jha'
for letter in name:
    if(letter=='h'):
        continue
    print(letter)