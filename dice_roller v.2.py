import random

n = input("Do you want to roll a dice? Yes or No: ")
while n == "Yes":
  if n =="Yes":
    m = int(input("How many? "))
    count = 0
    while count < m:

      sides = [*range(1,7,1)]
      #print(sides)
      a = random.choice(sides)
      print(a)
      count += 1 
  n = (input("Do you want to roll a dice? Yes or No: "))
  if n == "No":
    print("Thanks for playing")
    break