import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

playerchoice = input('Enter... \n1 for Rock,\n2 for Paper\n3 for Scissors:\n\n')
player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit('You must enter 1,2 or 3.')

computerchoice = random.choice('123')
computer = int(computerchoice)

print('')
print('You chose ' + str(RPS(player)).replace('RPS.', '').title() + '.')
print('Python chose ' + str(RPS(computer)).replace('RPS.', '').title() + '.')
print('')

YOU_WIN = 'You win!'

if player == 1 and computer == 3:
    print(YOU_WIN)
elif player == 2 and computer == 1:
    print(YOU_WIN)
elif player == 3 and computer == 2:
    print(YOU_WIN)
elif player == computer:
    print('Draw!')
else:
    print('Python wins!')
