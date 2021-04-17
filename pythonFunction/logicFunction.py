def even_check(num):
    return num%2==0
print(even_check(20))
print(even_check(45))
print(even_check(0))

my_list =[1,3,5,7,1]
def even_check_list(my_list):
    result = False;
    for num in my_list:
        print(num)
        if num%2==0:
            result = True
    return result

print(f'List contain even number {even_check_list(my_list)}')
    
    