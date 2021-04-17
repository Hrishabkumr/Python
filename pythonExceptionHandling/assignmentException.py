
try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print('There is some error occurred')

try:  
    x= 5
    y= 0
    z = x/y
except ZeroDivisionError:
    print('Division by zero error')
finally:
    print('All Done')
    
while True:
    try:
        num = int(input('Input an integer : '))
    except:
        print('An Occurred : Please try again')
        continue
    else:
        print(f'Thank you, your number squared is {num**2}')
        break