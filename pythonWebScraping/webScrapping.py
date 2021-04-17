import requests
result = requests.get("http://www.example.com/")

print(f'Type of Request : {type(result)}')
print(f'Request text ::::-> \n {result.text}')
