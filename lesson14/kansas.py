from random import choice

capital = "Topeka"

bird = "Western Meadowlark"


def randomfunfact():
    funfacts = ["1st", "2st", "3rd", "4th", "5th"]

    index = choice("01234")

    print(funfacts[int(index)])


if __name__ == "__main__":
    randomfunfact()
