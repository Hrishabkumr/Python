def generate_fibo(n):
    
    a = 0
    b = 1
    fibo_list = []
    for n in range(n+1):
        
        if(a>=n):
            break
        else:
            fibo_list.append(a)
            fibo_list.append(b)
            a = a+b
            b= a+b
        
    return fibo_list

number = int(input('Please enter the number : '))
print(generate_fibo(number))

    