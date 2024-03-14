from random import choice
import argparse
import sys

parser = argparse.ArgumentParser(description="Add your name using -n or --name flag")
parser.add_argument("-n", "--name", help="Player name", required=True)


player_wins = 0
game_count = 0

args = parser.parse_args()
playername = args.name


def guess_my_number(player_name="PlayerOne"):
    global player_wins
    global game_count
    print(f"{player_name}, guess which number I'm thinking of... 1, 2, or 3.")

    player_input = input("\n")
    random_value = choice("123")
    print(f"\n{player_name} You choose {player_input}.")
    print(f"I was thinking about the number {random_value}.")

    game_count += 1

    if player_input == random_value:
        player_wins += 1
        print(f"{player_name} You won")
    else:
        print(f"\nSorry, {player_name}. Better luck next time.")

    print(f"\nGame count: {game_count}")

    print(f"\n{player_name} wins: {player_wins}")

    percentage = 0

    if player_wins > 0:
        percentage = (player_wins / game_count) * 100

    print(f"\nYour winning percentage: {percentage:.2f}%")

    print(f"\nPlay again, {player_name}?")

    print("\nY for Yes or")
    print("Q for Quit")

    while True:
        playagain = input("")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain == "y":
        guess_my_number(player_name=player_name)
    else:
        if __name__ == "__main__":
            sys.exit(f"Thanks for playing, bye {player_name}.")
        else:
            return


if __name__ == "__main__":
    guess_my_number(playername)
