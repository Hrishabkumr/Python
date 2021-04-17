def func():
    print('from one.py func()')

print('top level in one.py')

if __name__=="__main__":
    print('one.py is being run directly')
else:
    print('one.py has been imported')