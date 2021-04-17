def create_cubes(n):
    
    for x in range(n):
        yield x**3

for x in create_cubes(5):
    print(x)
print('Fibonacci Series')  
def gen_fibo(n):
    
    a = 0
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

for x in gen_fibo(5):
    print(x)   

print('::::::::: Generator one more example :::::::::') 
def simple_gen():
    
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g= simple_gen()

print('Print result using iterator ')
print(next(g))
print(next(g))   