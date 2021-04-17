'''
Return slop and distance between the line
'''

class Line():
    
    def __init__(self,cord1,cord2):
        self.cord1 = cord1
        self.cord2 = cord2
    
    def distance(self):
        (x1,y1) = self.cord1
        (x2,y2) = self.cord2
        
        dist = ((y2-y1)**2+(x2-x1)**2)**0.5
        print(f'Distance between line is : {dist:1.3f}')
    
    def slope(self):
        (x1,y1) = self.cord1
        (x2,y2) = self.cord2
        
        m = (y2-y1)/(x2-x1)
        print(f'Slop of line is : {m}')

cordinate1 = (3,2)
cordinate2 = (8,10)

line = Line(cordinate1,cordinate2)

line.distance()

line.slope()

    