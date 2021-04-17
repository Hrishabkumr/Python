def vol(rad):
    return (4/3)*(22/7)*(rad**3)
radius = 2 
print(f'The volume of sphere with radius {radius} is {vol(radius):1.3f}')

def ran_check(num,low,high):
    if(num>low and num<high):
        print(f'{num} is in the range between {low} to {high}')
    else:
        print(f'Out of range')
        
ran_check(2, 5, 7)
ran_check(2, 1, 7)

print('Number of uppercase or lowercase letter')
def up_low(text):
    upperCaseCount = 0
    lowerCaseCount = 0
    for letter in text:
        if(letter.isupper()):
            upperCaseCount+=1
        elif (letter.islower()):
            lowerCaseCount+=1
    print(f'Text : {text}')
    print(f'Total uppercase letter : {upperCaseCount}\nTotal lowercase letter : {lowerCaseCount}')

up_low('Hello And Welcome to Python Tutorial') 

print('Return unique list from list')
def unique_list(num_list):
    return list(set(num_list))

num_list = [1,2,3,1,1,2,34,43,3,2,23,4]
print(f'Actual list : {num_list}') 
uni_list = unique_list(num_list)
print(f'Unique list : {uni_list}')  

