class Cylinder():
    
    pi = 3.14
    
    def __init__(self, height=1, radius=1):
        print('Calculating Cylinder volume and surface area ')
        self.height = height
        self.radius = radius
    
    def volume(self):
        vol = self.pi * self.radius ** 2 * self.height
        print(f'Volume of Cylinder {vol}')
    
    def surface_area(self):
        area = 2 * self.pi * self.radius * self.height + 2 * self.pi * self.radius ** 2
        print(f'Area of Cylinder {area}')


cylinder = Cylinder(2, 3)

cylinder.volume()

cylinder.surface_area()
