
# ---- TASK ONE: GENEREATE RANDOM MATH PROBLEMS ------ [COMPLETE]
from fractions import Fraction
import random

randomNum1 = random.randint(0,20)
randomNum2 = random.randint(0,20)
listOfOperations = ["x", "+", "-", "/"]
i = random.randint(0,3)
randomOperation = listOfOperations[i]

def randomSequence(randomNum1, randomNum2, randomOperation):
    if randomOperation == "x":
        print("THE ANSWER:  " + str(randomNum1 * randomNum2))
    elif randomOperation == "+":
            print("THE ANSWER: " + str(randomNum1 + randomNum2))
    elif randomOperation == "/":
         print("THE ANSWER: " + str(Fraction(randomNum1 / randomNum2)))
    else:
         print("THE ANSWER: " + str(randomNum1 - randomNum2))
    return(str(randomNum1) + " " + str(randomOperation) + " " + str(randomNum2) + " = ")

# ---- TASK TWO: CHARACTER SPEED CHANGES UPON GOLD CONSUMPTION ------ [COMPLETE]

correctAnswer = bool

def increasePlayerSpeed(correctAnswer):
    playerXSpeed = 10
    if correctAnswer:
        playerXSpeed = playerXSpeed + 10 #player speeds up upon correct answer
        print(playerXSpeed) #for testing purposes
    else:
        playerXSpeed = playerXSpeed - 10 #player slpws down upon incorrect answer
        print(playerXSpeed) #for testing purposes

# increasePlayerSpeed(False) #for testing purposes

    