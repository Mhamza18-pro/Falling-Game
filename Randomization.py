
# ---- TASK ONE: GENEREATE RANDOM MATH PROBLEMS ------ [COMPLETE]
import random

randomNum1 = random.randint(0,20)
randomNum2 = random.randint(0,20)
listOfOperations = ["x", "+", "-", "/"]
i = random.randint(0,3)
randomOperation = listOfOperations[i]

def randomSequence():
    print(str(randomNum1) + " " + str(randomOperation) + " " + str(randomNum2) + " = ")

randomSequence()

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

increasePlayerSpeed(False) #for testing purposes
    