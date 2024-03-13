import sys
import random
from enum import Enum

global_count = 0

def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input('Enter... \n1 for Rock,\n2 for Paper\n3 for Scissors:\n\n')

    if playerchoice not in ['1', '2', '3']:
        print('You must enter 1,2 or 3.')
        return play_rps()

    player = int(playerchoice)

    computerchoice = random.choice('123')
    computer = int(computerchoice)

    print('')
    print('You chose ' + str(RPS(player)).replace('RPS.', '').title() + '.')
    print('Python chose ' + str(RPS(computer)).replace('RPS.', '').title() + '.')
    print('')

    YOU_WIN = '🎉 You win!'

    if player == 1 and computer == 3:
        print(YOU_WIN)
    elif player == 2 and computer == 1:
        print(YOU_WIN)
    elif player == 3 and computer == 2:
        print(YOU_WIN)
    elif player == computer:
        print('😧 Draw!')
    else:
        print('🐍 Python wins!')

    global global_count
    global_count += 1
    print('\n Game count: ' + str(global_count))

    print('\nPlay again?')

    while True:
        playagain = input('\nY for Yes or \nQ to Quit\n')
        if playagain.lower() not in ['y', 'q']:
            continue
        else:
            break

    if playagain.lower() == 'y':
        play_rps()
    else:
        sys.exit('Thank you for playing... Bye 👋')

play_rps()