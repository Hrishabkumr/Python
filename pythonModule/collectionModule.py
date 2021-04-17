from collections import Counter, namedtuple
from _collections import defaultdict

list = [1,2,2,2,3,4,5,6,7,8,8,10,'a','a','b',10]
print(Counter(list))

name = 'Hrishabkumar Jha'
print(Counter(name))

sentence = 'How many times how word is repeated in a sentence'
print(Counter(sentence.lower().split()))

Dog = namedtuple('Dog',['age','breed','name'])
sammy  = Dog(age=5,breed='Husky',name='Sam')
print(sammy.age)


d = defaultdict(lambda: 0)
d['correct'] = 100

print(d['correct'])
print(d['wrong key'])