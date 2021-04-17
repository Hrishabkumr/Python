'''
Created on Nov 16, 2020

@author: Asus
'''

t = (1,2,3,1,1,1,1)
my_list = [1,2,3]

print(f'Type t{type(t)}')
print(f'Type my_list{type(my_list)}')

print(t.count(1))
print(t.index(2))

#'tuple' object does not support item assignment
t[0] = 2;
