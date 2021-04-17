try:
    #give an error
    result = 10+'10'
    print(f'Result = {result}')
except:
    print('Hey there is some ERROR!!!')
finally:
    print('from finally block')