import math

value = math.pi
print(value)

width = 1
while(True):
    precision = int(input('Enter the number of digit want after decimal : '))
    
    print(precision)
    if precision>10:
        break
    else:
        print(f"result: {value:{width}.{precision}}")
        
print('Done')
