def multiply(nums):
    result = 1
    for num in nums:
        result = result* num
    return result

nums = [1,2,3,-4]
result = multiply(nums)
print(f' Multiplication result : {result}')