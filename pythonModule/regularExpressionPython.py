import re 
text = 'hello and welcome to my world'

pattern = 'hello'
result = re.search(pattern, text)
print(f'Is Exist {result}')

text = 'a phone once, a phone twice'
match = re.search('phone',text)
print(f'{match}')

print('To find all the occurrence in a string')
matches = re.findall('phone', text)
print(f'Matches : {matches}')

text = 'My phone number is 8823-0454-36'
match = re.search(r'\d\d\d\d-\d\d\d\d-\d\d', text)
print(f'Match {match}')
print(f'Phone number : {match.group()}')

match = re.search(r'\d{4}-\d{4}-\d{2}', text)
print(f'Match {match}')
print(f'Phone number : {match.group()}')

phone_pattern = re.compile(r'(\d{4})-(\d{4})-(\d{2})')
match = re.search(phone_pattern, text)
print(f'{match.group()}')
print(f'Get first group : {match.group(1)}')


print('------ Multiple pattern search -------')
match = re.search(r'cat|dog','The cat dog is an animal')
print(f'Matches {match}')

match = re.findall(r'cat|dog','The cat dog is an animal')
print(f'All matches {match}')

print('----- Find using dot(.) pattern or start with -----')
match = re.findall(r'^\d','1 is number')
print(f'Result {match}')

print('----- Find using $ pattern or end with -----')
match = re.findall(r'\d$','one is number 1')
print(f'Result {match}')

print('---- To exclude the number from the phrase ----')
phrase = 'This is sentence with 3 number 34 in 5 in 12'
pattern = r'[^\d]+'
match = re.findall(pattern,phrase)
print(f'Result excluded number : {match}')

