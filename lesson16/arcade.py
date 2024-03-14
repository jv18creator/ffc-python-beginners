# Arcade (Main file)
import argparse
from guess_number import guess_my_number
from rps import rock_paper_scissors

parser = argparse.ArgumentParser(description="Your name")


def run_arcade():
    parser.add_argument("-n", "--name", required=True)
    args = parser.parse_args()
    player_name = args.name
    print(f"\n{player_name}, welcome to the Arcade!")

    while True:
        print("\nPlease choose a game:")
        print("1 = Rock Paper Scissors")
        print("2 = Guess My Number")
        print('\nOr press "x" to exit the Arcade')

        game = input("")

        if game == "1":
            rock_paper_scissors(name=player_name)
        elif game == "2":
            guess_my_number(player_name=player_name)
        elif game.lower() == "x":
            print(f"Bye {player_name}")
            break
        else:
            print("Invalid input. Please choose again.")


run_arcade()
