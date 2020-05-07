# form youtubevideo http://youtu.be/miuHrP2O7Jw

import random
import time

def intro():
  print("==================")
  print("Game starting here")
  print("==================")
  time.sleep(3)
  print("In front of you is one of the biggest building you have ever seen.")
  time.sleep(3)
  print("This is gotta be the place. The one they are talking about in town.")
  time.sleep(3)
  print("The castle, a maze of rooms, and at the end...")
  time.sleep(3)
  print("At the end. A trassure. Capable of forfilling your every wish.")
  time.sleep(3)
  print('"What would i wish for?" you think quietly.. I need this...')
  time.sleep(3)
  print("Im already so far along,! But its so dark and scary!")
  time.sleep(4)
  print("There is a giant door right in front of you, ")
  x = input("do you want go in? yes or no")
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





