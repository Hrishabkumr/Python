class Calc():
    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def add(self,num1,num2):
        return num1+num2
    
    def sub(self,num1,num2):
        return num1-num2
    
    def multi(self,num1,num2):
        return num1*num2
    
    def div(self,num1,num2):
        
        if(num2==0):
            return 'Division Error!!!'
        else:
            return num1/num2

calc = Calc(10,20)

print(f'Addition result {calc.add(10, 20)}')
print(f'Substraction result {calc.sub(10, 20)}')
print(f'Multi result {calc.multi(10, 20)}')
print(f'Division result {calc.div(10, 0)}')
