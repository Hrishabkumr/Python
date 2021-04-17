class Animal():
    
    def __init__(self):
        print('Animal Class created')
    
    def who_am_i(self):
        print('I m an animal')
    
    def eat(self):
        print('I am eating')

class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print('Dog class created')
    
    def eat(self):
        print('Dog eating food')
    
dog = Dog()

dog.eat()
dog.who_am_i()