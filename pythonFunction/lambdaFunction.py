print('Before using lambda expression')
def square(nums):
    return nums**2

nums_list = [1,2,3,4]
square_list = list(map(square,nums_list))
print(f'Square list : {square_list}')

print('Converting square function to lambda expression')
square_lambda = lambda nums:nums**2

print(f'Square using lambda {list(map(square_lambda,nums_list))}')