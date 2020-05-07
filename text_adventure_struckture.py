import random
import time

def intro():
  print("You are at the entrance")
      

def chosePath1():
  path = ""
  while path != "1" and path != "2":
    path = input("Do you wanna go to room 1 or room 2? (Type 1 og 2) ")
  return path

def room1(userChoice):
  if userChoice == "1":
    print("Filler text room 1")

def room2(userChoice):
  if userChoice == "2":
    print("Filler text room 2")

def chosePath2():
  path2 = ""
  while path2 != "3" and path2 != "4":
    path2 = input("Do you wanna go to room 3 or room 4? (Type 3 og 4) ")
  return path2

def room3(userChoice2):
  if userChoice2 == "3":
    print("Filler text room 3")
    

def room4(userChoice2):
  if userChoice2 == "4":
    print("Filler text room4")







def playAgain():
  x = ""
  while x != "yes" and x != "y":
    x = input("Do you want to play? yes og y to start, no to quit:  ")
    if x == "no":
      exit(0)


playAgain()
intro()
#correctPath()
userChoice = chosePath1()
room1(userChoice)
room2(userChoice)
userChoice2 = chosePath2()
room3(userChoice2)
room4(userChoice2)

