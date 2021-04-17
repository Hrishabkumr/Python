import random

def display_board(board):
    print('------------------')
    print(board[7] + '|' + board[8] + '|' + board[9])
    print(board[4] + '|' + board[5] + '|' + board[6])
    print(board[1] + '|' + board[2] + '|' + board[3])

def player_input():
    
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1,Please select input X or O: ')
    
    player1_marker = marker
    if player1_marker == 'X':
        player2_marker = 'O'
    else:
        player2_marker = 'X'
    
    return (player1_marker, player2_marker)

def place_marker(board, marker, POSITION):
    board[POSITION] = marker

def win_check(board, mark):
    return (board[1] == board[2] == board[3] == mark or
           board[4] == board[5] == board[6] == mark or
           (board[7] == board[8] == board[9] == mark) or
           (board[7] == board[4] == board[1] == mark) or
           (board[8] == board[5] == board[2] == mark) or
           (board[9] == board[6] == board[3] == mark) or
           (board[1] == board[5] == board[9] == mark) or
           board[7] == board[5] == board[3] == mark)
           
def choose_first():
    flip = random.randint(0, 1)
    
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board, POSITION):
    
    return board[POSITION] == ' '

def full_board_check(board):
    for POSITION in range(1, 10):
        if space_check(board, POSITION):
            return False
    return True

def player_choice(board):
    
    POSITION = 0
    while POSITION not in range(1, 10) or not space_check(board, POSITION):
        POSITION = int(input('Choose a POSITION : (1-9) '))
    
    return POSITION

def replay():
    
    choice = input('Are you want the game again choose Yes or No: ')
    return choice == 'Yes'
    
print('Welcome to Tic tac Toe game')

while True:
    
    # play the game
    # #set everything up (Board ,who is first, choose marker X or  O
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    
    turn = choose_first()
    print(turn + ' will be first')
    
    play_game = input('Ready to play the game ? y or n ')
    # #Game play
    if play_game == 'y':
        GAME_ON = True
    else:
        GAME_ON = False
    
    while GAME_ON:
        if turn == 'Player 1':
              # #Player 1 turn
              # show the board
              display_board(the_board)
              # choose a POSITION
              
              POSITION = player_choice(the_board)
              # place the marker on the POSITION
              
              place_marker(the_board, player1_marker, POSITION)
              # check if they won
              
              if win_check(the_board, player1_marker):
                  display_board(the_board)
                  print('Player 1 Won!!!')
                  GAME_ON = False
              else:
                  if full_board_check(the_board):
                      display_board(the_board)
                      print('Game is tie!!')
                      GAME_ON = False
                  else:
                      turn = 'Player 2'
              # or check if there is a tie
              
              # no tie and no win? The next player turn 
    
        else:
            # #Player 2 turn
            # show the board
              display_board(the_board)
              # choose a POSITION
              
              POSITION = player_choice(the_board)
              # place the marker on the POSITION
              
              place_marker(the_board, player2_marker, POSITION)
              # check if they won
              
              if win_check(the_board, player2_marker):
                  display_board(the_board)
                  print('Player 1 Won!!!')
                  GAME_ON = False
              else:
                  if full_board_check(the_board):
                      display_board(the_board)
                      print('Game is tie!!')
                      GAME_ON = False
                  else:
                      turn = 'Player 1'
    
    if not replay():
        break
    
