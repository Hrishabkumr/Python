import string

def check_palindrome(word):
    actual_str = word
    result_str = word[::-1]
    if actual_str==result_str:
        print('String is palindrome')
    else:
        print('String is not palindrome')

check_palindrome('madam')

print(string.ascii_lowercase)
    