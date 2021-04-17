def prime_factor(n):
    factor = []
    prime_factor = []
    for num in range(2,n+1):
        if(n%num==0):
            factor.append(num)
           
    for num in factor:
        isPrime = True
        for fac in range(2,num):
            if(num%fac==0):
                isPrime = False
                break
        if(isPrime):
            prime_factor.append(num)

    return prime_factor

print(prime_factor(119))