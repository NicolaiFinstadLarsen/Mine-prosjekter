# form youtubevideo http://youtu.be/miuHrP2O7Jw

import random
import time

def intro():
  print("==================")
  print("Game starting here")
  print("==================")
  time.sleep(1)
  print("Lets go!")
  time.sleep(2)
  print()

def chosenPath():
  path = ""
  while path != "1" and path != "2": #input validation, hvis den eller den er True. Kjør.
    path = input("Which path do you choose? 1 or 2 ")
    print()

  return path

def checkPath(chosenPath):
  print("Going down path")
  time.sleep(2)
  print("A big shining light!")
  time.sleep(2)
  print("Is that a good sign? Hmmm....")
  time.sleep(2)
  print()

  correctPath = random.randint(1,2)

  if chosenPath == str(correctPath):
    print("Its the gold at the end of the rainbow!!")
    time.sleep(1)
    print("You've won the game")
    time.sleep(2)
    print()
  else:
    print("Shit! Its a fucking train!")
    time.sleep(1)
    print("You dieded")
    time.sleep(2)
    print()

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":

  intro()
  choice = chosenPath()
  checkPath(choice) # choice is equal to "1" or "2"
  playAgain = input("Do you want to play again? Yes or y to continue ")
