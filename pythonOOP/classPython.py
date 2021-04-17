class Dog():
     
     #class level attributs
     species = 'Mammal'
     def __init__(self,breed,name,spots):
         self.breed = breed
         self.name = name
         self.spots = spots
         
     def bark(self):
        print(f'WOOF!! My dog name is {self.name}')

my_dog = Dog(breed='German',name='Dustie',spots=False)

print(type(my_dog))
print(f'Breed : {my_dog.breed} \nName : {my_dog.name} \nSpots : {my_dog.spots} \nSpecies {my_dog.species}')
my_dog.bark()