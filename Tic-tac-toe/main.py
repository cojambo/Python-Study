import os
import random
from colorama import Fore

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
playewins = 0
CPUwins = 0

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
Player wins: {Fore.CYAN + str(playewins) + Fore.RESET}  
CPU wins: {Fore.LIGHTMAGENTA_EX + str(CPUwins) + Fore.RESET}
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
                screen()
                print('Invalid Position')
                l = int(input('Row: '))
                c = int(input('Column: ')) 
            board[l][c] = 'X'
            plays += 1
            whoplay = 1
        except:
            print('invalid row and/or column')


def cpu():
    global maxplays
    global plays
    global whoplay
    if whoplay == 1 and plays<maxplays:
            l = random.randrange(0,3)
            c = random.randrange(0,3)    
            while board[l][c] != ' ':
                l = random.randrange(0,3)
                c = random.randrange(0,3)
            board[l][c] = 'O'
            plays += 1
            whoplay = 2

def wincheck():
    global win
    symbols = ['X','O']
    for s in symbols:
        win = 'n'
        l=c=0
        #Rows check
        while l < 3:
            plus = 0
            c = 0
            while c < 3:
                if (board[l][c]==s):
                    plus += 1  
                c +=1
            l += 1
            if plus == 3:
                win = s
                break
        if win != 'n':
            break
        #Columns check
        win = 'n'
        l=c=0
        while c < 3:
            plus = 0
            l = 0
            while l < 3:
                if (board[l][c]==s):
                    plus += 1  
                l +=1
            c += 1
            if plus == 3:
                win = s
                break
        if win != 'n':
            break
        
        #DIAGONAL CHECK
        plus = 0
        d1 = 0
        l=c= 0
        while d1 < 3:
            if board[l][c]==s:
                plus += 1
            l += 1
            c += 1
            d1 +=1
            if plus ==3:
                win = s
                break
        if win != 'n':
            break         
        
        plus = 0
        d2 = 0
        l = 0
        c = 2
        while d2 < 3:
            if board[l][c]==s:
                plus += 1
            l += 1
            c -= 1
            d2 +=1
            if plus ==3:
                win = s
                break
        if win != 'n':
            break        
    return win

def reset():
    global playagain
    global plays
    global maxplays
    global win
    global whoplay
    global board
    plays = 0
    maxplays = 9
    win = 'n'
    whoplay = 2 # 1 == CPU, 2 == PLAYER
    board = [
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
    ]

wincheck()

while True:
    screen()
    player()
    cpu()
    winc = wincheck()
    match winc:
        case 'X':
            playewins += 1
        case 'O':
            CPUwins += 1
    screen()
    if winc != 'n' or maxplays <= plays:
        print(f'{winc} win the game!')
        playagain = input('Play again? (y/n)')
        reset()
        if playagain == 'n':
            if playewins > CPUwins:
                print(Fore.CYAN + 'Player is the winner!' + Fore.RESET)
            elif CPUwins > playewins:
                print(Fore.LIGHTMAGENTA_EX + 'CPU is the winner!' + Fore.RESET)
            else:
                print(Fore.LIGHTRED_EX + 'Game tied' + Fore.RESET)
            break
