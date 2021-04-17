def square(nums):
    return nums**2

num_list = [1,2,3,4]
square_list = list(map(square,num_list))
print(f'Square Values : {square_list}')

def check_string(string):
    if(len(string)%2==0):
        return 'Even'
    else:
        return string[0]
    
string_list = ['hrishab','jha','amar']
new_list = list(map(check_string,string_list))
print(f'String list : {new_list}')