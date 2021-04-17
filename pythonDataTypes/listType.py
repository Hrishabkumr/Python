my_list = ['apple','mango','banana']
print(f'List size {len(my_list)}')

print(my_list[1:])

another_list = ['cake','chocolate']
new_list = my_list+another_list

print(new_list)

print(new_list.pop())

print(new_list)

print(new_list.pop(2))

print(new_list)

new_list = ['a','e','z','b','g']
num_list = [1,4,8,2,0]

new_list.sort()
num_list.sort()
print(f'The sorted list {new_list}')
print(f'The sorted number list {num_list}')

num_list.reverse()
print(f'The reverse list {num_list}')