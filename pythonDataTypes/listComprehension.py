mystring = "hrishabkumar jha"
my_list = []
for letter in mystring:
    my_list.append(letter)
print(my_list)

#using comprehension
my_list = [num for num in range(0,10)]
print(my_list)

my_list = [letter  for letter in mystring]
print(my_list)

#Even number
my_list = [num for num in range(0,10) if num%2==0]
print(my_list)

my_list = [num**3 for num in range(0,11)]
print(my_list)

