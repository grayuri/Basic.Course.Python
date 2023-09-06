import sys
import random

firstNumber = random.randint(0,10)
secondNumber = random.randint(0,10)
thirdNumber = random.randint(0,10)
fourthNumber = random.randint(0,10)
fifthNumber = random.randint(0,10)

tuple = (firstNumber, secondNumber, thirdNumber, fourthNumber, fifthNumber)

lowestNumber = 11
lowestNumberIndex = 0
highestNumber = -11
highestNumberIndex = 0

for index, number in enumerate(tuple):
  if number < lowestNumber: 
    lowestNumber = number
    lowestNumberIndex = index

  if number > highestNumber: 
    highestNumber = number
    highestNumberIndex = index

print(f"The drawn tuple is {tuple}")
print(f"- The lowest number of the tuple is {lowestNumber}, he is in the position {lowestNumberIndex + 1}.")
print(f"- The highest number of the tuple is {highestNumber}, he is in the position {highestNumberIndex + 1}.")