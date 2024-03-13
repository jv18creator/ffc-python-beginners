import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input("Enter... \n1 for Rock,\n2 for Paper\n3 for Scissors:\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1,2 or 3.")
            return play_rps()

        player = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print("")
        print(f"\nYou chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python chose {str(RPS(computer)).replace('RPS.', '').title()}.")
        print("")

        YOU_WIN = "🎉 You win!"

        if player == 1 and computer == 3:
            player_wins += 1
            print(YOU_WIN)
        elif player == 2 and computer == 1:
            player_wins += 1
            print(YOU_WIN)
        elif player == 3 and computer == 2:
            player_wins += 1
            print(YOU_WIN)
        elif player == computer:
            print("😧 Draw!")
        else:
            python_wins += 1
            print("🐍 Python wins!")

        nonlocal game_count
        game_count += 1
        print(f"\n Game count: {str(game_count)}")
        print(f"\n Player wins: {str(player_wins)}")
        print(f"\n Python wins: {str(python_wins)}")

        print("\nPlay again?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            play_rps()
        else:
            sys.exit("Thank you for playing... Bye 👋")

    return play_rps()


rock_paper_scissors = rps
if __name__ == "__main__":
    rock_paper_scissors()
