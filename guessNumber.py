import random

tentative = 0
tentativeMax = 10
levels = [(1, 50), (2, 100), (3, 1000)]

print("Welcome to the game! You have to guess a number")

def selectLevel():
    print("Select the level!")
    print(f"1. Number from 0 to {levels[0][1]}")
    print(f"2. Number from 0 to {levels[1][1]}")
    print(f"3. Number from 0 to {levels[2][1]}")

    while True:
        try:
            levelChoice = int(input("Select level : "))
            if levelChoice >= 1 and levelChoice <= 3:
                print(f"You have to guess a number from 0 to {levels[levelChoice - 1][1]}")
                return levelChoice
            else:
                print("Select a correct level")
        except ValueError:
            print("Input non valid")
            continue

def generateNumber(level):
    if level == 1 or level == 2 or level == 3:
        return random.randint(0, levels[level - 1][1])

def inputGuess():

    while True:
        try:
            numberGuessing = int(input("Try to guess the number : "))
            if numberGuessing < 0 or numberGuessing > levels[levelChoice - 1][1]:
                print("Input not valid")
                continue
            else:
                return numberGuessing
        except ValueError:
            print("Input non valid")
            continue

def checkGuess(numberToGuess, numberGuessing):
    if numberGuessing < numberToGuess:
        print("Your number is lower than the target")
        return True
    elif numberGuessing > numberToGuess:
        print("Your number is higher than the target")
        return True
    else:
        return False

def playAgain():
    choice = input("1 to play again, any key to exit : ")

    if choice == '1':          
        return True
    else:
        print("Goodbye!")
        return False

def tentativeRemaining(tentative, tentativeMax, numberToGuess):
    if tentativeMax - tentative == 0:
        print("You have lost!")
        return False
    else:
        if tentative == 5:
            if numberToGuess % 2 == 0:
                print("The number that you have to guess is even!")
            else:
                print("The number that you have to guess is not even!")
        print(f"You have {tentativeMax - tentative} tentatives remaining!")
        return True

def score(tentative):
    print(f"You have scored {(tentativeMax - tentative) * 100} points")

while True:

    levelChoice = selectLevel()
    numberToGuess = generateNumber(levelChoice)
    numberGuessing = inputGuess()

    while True:
        tentative += 1
        check = checkGuess(numberToGuess, numberGuessing)

        if check:
            checkTentativeRemaining = tentativeRemaining(tentative, tentativeMax, numberToGuess)
            if checkTentativeRemaining:
                numberGuessing = inputGuess()
                continue
            else:
                print("Game over")
                break
        else:
            score(tentative)
            print(f"You have guessed the number after {tentative} tentative!")
            break

    play = playAgain()
    if play == True:
        tentative = 0
        continue
    else:
        break           
    