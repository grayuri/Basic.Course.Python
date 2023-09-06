import random

numbersToThink = [0, 1, 2, 3, 4, 5]

whatTheComputerThink = random.choice(numbersToThink)

print('The computer thought a number between 0 and 5.')

whatIthink = int(input('What number you think he thought? '))

if whatIthink == whatTheComputerThink:
  print('WOW! You hit it!')
else:
  print("That's a shame. He thought the number {}. Maybe in another time you can do it right.".format(whatTheComputerThink))