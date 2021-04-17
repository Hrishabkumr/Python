def hello(name):
    
    print('Welcome to hello method')
    
    def greet():
        print('Welcome to greet method')
    
    def welcome():
        print('This is from welcome method')
    
    if name=='Hrishab':
        return greet
    else:
        return welcome
    
    print('End of hello method')

my_func = hello('Hrishab')
my_func()
