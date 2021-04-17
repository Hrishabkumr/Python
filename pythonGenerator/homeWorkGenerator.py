import random
print(':::: Generator Homework ::::')
print(':::: Generate square of certain number :::')

def gen_square(n):
    
    for x in range(n+1):
        yield x**2

for number in gen_square(5):
    print(number)

print(':::: Generate random number between low and high :::')    
def gen_rand_num(low,high,n):
    
    for i in range(n):
        yield random.randint(low,high)

for num in gen_rand_num(1, 12, 10):
    print(num)

print(':::: Generate String iterator :::')

s = 'hrishabkumar'
s_iter = iter(s)
print(list(s_iter))
