import random
from lib.game import Game
import time
from lib.styles import theMenu, welcomeMessage
import sys

class Main:
    def __init__(self) -> None:
        print(welcomeMessage)
        self.menu()

    def menu(self):
        userMenuInput = input(theMenu)
        if userMenuInput == "1":
            self.start()
        elif userMenuInput == "2":
            self.rules()
        elif userMenuInput == "3":
            self.quit()
        
    def start(self):
        Game()
        self.menu()

    def rules(self):
        print("")
        print("The whole point of the game is to guess the number the computer is holding...(1/5)")
        time.sleep(4)
        print("The guess ranges between 1 - 100...(2/5)")
        time.sleep(4)
        print("Every time you guess incorrect, the programme tells you higher or lower...(3/5)")
        time.sleep(4)
        print("You have 6 lives. Every incorrect answer loses a life...(4/5)")
        time.sleep(4)
        print("If you reach 0 lives, then you lose. But if you guess correct answer before that you win! Simple...(5/5)")
        self.menu()

    def quit(self):
        sys.exit()

Main()