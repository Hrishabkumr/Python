#initialize list
from random import shuffle
bucket = ['O',' ', ' ']

def shuffle_list(bucket):
    shuffle(bucket)
    return bucket

def  check_guess(bucket,guess):
    if(bucket[guess]=='O'):
        print('Correct Guess')
    else:
        print('Wrong Guess...Booooo')
        print(f'Actual list {bucket}')
        
def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input('Kindly enter number from 0,1 or 2 ')
    return int(guess)

#shuffle list
bucket = shuffle_list(bucket)
#user guess
guess = player_guess()    
#check quess
check_guess(bucket, guess)