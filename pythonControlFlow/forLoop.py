num_list = [1,2,3,4,5,6,7,8,9]
for num in num_list:
    print(num)
    
for num in num_list:
    #check for even
    if(num%2==0):
        print(f'Even number : {num}')
    else:
        print(f'Odd number : {num}')

print('------Calculate total list sum------')     
listSum=0;
for num in num_list:
    listSum+=num
print(f'Total Sum = {listSum}')
    
print('------Iterate String------')
name = 'Hrishabkumar Jha'
for letter in name:
    print(letter)

print('------Iterate Tuple------')
my_list = [(1,2),(3,4),(5,6),(7,8)]
for tup in my_list:
    print(tup)
    
print('------Tuple Unpacking------')
my_list = [(1,2),(3,4),(5,6),(7,8)]
for (a,b) in my_list:
    print(a)
    print(b)
    
print('------Iterate Dictionary------')
d = {'k1':1,'k2':2,'k3':3}
for item in d.items():
    print(item)

print('------Iterate Dictionary print key and value------')
d = {'k1':1,'k2':2,'k3':3}
for key,value in d.items():
    print(key)
    print(value)
    
print('------Iterate Dictionary print only value------')    
for value in d.values():
    print(value)