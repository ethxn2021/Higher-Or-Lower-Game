import random
from lib.styles import *

class Game:
    def __init__(self) -> None:
        self.computerNumber = ""
        self.lives = 6
        self.startGame()

        


    def generateNewNumber(self):
        randomNumber = random.randint(0,99)
        self.computerNumber = randomNumber

    def userGuess(self):
        userAnswer = input(colored("\nWhat number I'm I thinking? \n{}\nGuess:".format(colored("Lives: " + str(self.lives),"red")),"blue"))
        userAnswer = int(userAnswer)
        self.checkValue(userAnswer)


    def checkValue(self,value):
        if value == self.computerNumber:
            print(correctMessage)
            return
            
        else:
            self.lives -= 1
            if value < self.computerNumber:
                print(higherMessage)
            elif value > self.computerNumber:
                print(lowerMessage)

        self.checkLives(self.lives)
        self.userGuess()

    def checkLives(self,lives):
        if self.lives < 1:
            print(gameOverMessage)

    def startGame(self):
        self.generateNewNumber()
        self.userGuess()

