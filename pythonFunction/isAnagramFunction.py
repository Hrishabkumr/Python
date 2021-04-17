import string
def isAnagram(str1,alphabet = string.ascii_lowercase):
    # create a set of alphabet
    alphaset = set(alphabet)
    # remove any spaces from the input string
    str1 = str1.replace(' ','')

    # convert into all lowercase
    str1 = str1.lower()
    # grab all unique letters from the string set()
    str1 = set(str1)
    print(f'str1 = {str1}')
    print(f'alphaset = {alphaset}')
    # alphabet set == string set input
    return str1==alphaset

str1 = 'The quick brown fox jumps over the lazy dog' 
print(isAnagram(str1))
    