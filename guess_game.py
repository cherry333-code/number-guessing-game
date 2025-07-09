import random

def getRandomNumber():
    return random.randrange(1, 100)

def giveHint(number, guess):
    if guess == number:
        return "Right"
    elif number - 10 <= guess <= number + 10:
        return "Hot"
    else:
        return "Cold"

def runGuess():
    secretNumber = getRandomNumber()
    user_guess = int(input("Enter a number between 1 and 100: "))
    hint = giveHint(secretNumber, user_guess)
    if hint == "Right":
        print("You guessed it Right!")
    else:
        print(hint)

if __name__ == '__main__':
    runGuess()
