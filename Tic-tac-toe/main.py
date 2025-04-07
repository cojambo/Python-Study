import os
import random
from colorama import Style, Fore, Back

#Variables for use in the game
playagain = 'y'
plays = 0
maxplays = 9
win = 'n'
whoplay = 2 # 1 == CPU, 2 == PLAYER
board = [
    [' ',' ',' '],
    [' ',' ',' '],
    [' ',' ',' ']
]

def screen():
    os.system('cls')
    print(f'''
    0   1   2
0:  {board[0][0]} | {board[0][1]} |  {board[0][2]} 
   -----------
1:  {board[1][0]} | {board[1][1]} |  {board[1][2]}
   -----------
2:  {board[2][0]} | {board[2][1]} |  {board[2][2]}
plays: {Fore.GREEN + str(plays) + Fore.RESET}
''')

def player():
    global plays
    global whoplay
    global maxplays
    if whoplay == 2 and plays<maxplays:
        try:
            l = int(input('Row: '))
            c = int(input('Column: '))    
            while board[l][c] != ' ':
                print('Space already marked')
                l = int(input('Row: '))
                c = int(input('Column: ')) 
            board[l][c] = 'X'
            plays += 1
            whoplay = 1
        except:
            print('invalid row and/or column')
os.system('cls')
player()