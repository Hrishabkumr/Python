# Return an iterator yielding those items of iterable for which function(item)
#     is true. If function is None, return the items that are true.

def check_even(nums):
    return nums%2==0

numlist = [1,2,3,4,5,6]
even_list = list(filter(check_even,numlist))
print(f'Even list : {even_list}')

print(f'Iterating using for loop')
for num in even_list:
    print(num)