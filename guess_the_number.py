from random import randint

if __name__ == "__main__":
    number = randint(0, 1000)
    turns = 1

    print("Try to guess the chosen number from 0 to 1000: ", end='')
    guess = int(input())

    while guess != number:
        turns += 1
        hint = "greater" if number > guess else "lower"

        print('')
        print(f"Hint: The number is {hint} than your last guess")
        print("Try again: ", end='')

        guess = int(input())

    print("Congratulations!!!")
    print(f"You finished the game in {turns} turns")
