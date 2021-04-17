import  math

e_value = math.e
print(f'e value : {e_value}')

width = 1
while(True):
    
    precision = int(input('Please enter value : '))
    
    if precision>10:
        break
    else:
        print(f'Result : {e_value:{width}.{precision}}')
print('Done')