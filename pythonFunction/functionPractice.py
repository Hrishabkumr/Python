
def lesser_of_two_evens(num1,num2):
    if(num1%2==0 and num2%2==0):
        return min(num1, num2)
    else:
        return max(num1, num2)

print(f'Result : {lesser_of_two_evens(2, 4)}')
print(f'Result : {lesser_of_two_evens(2, 5)}')    

##Animal Crackers

def animal_crackers(text):
    words = text.lower().split()
    print(words)
    firstWord = words[0]
    secondWord = words[1]
    
    return firstWord[0]==secondWord[0]
    
print(f"First Word matched : {animal_crackers('Hrishab Hari')}")   
print(f"First Word matched : {animal_crackers('Hrishab Jha')}")

''' Makes Twenty problem '''
def makes_twenty(num1,num2):
    return (num1+num2==20) or num1==20 or num2==20
    
print(f'Result {makes_twenty(12,8)}')
print(f'Result {makes_twenty(20,8)}')
print(f'Result {makes_twenty(13,6)}')