import random

numbersToThink = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

whatTheComputerThink = random.choice(numbersToThink)

userWin = False
tries = 0

print('The computer thought a number between 0 and 10.')

while(userWin == False):

  whatIthink = int(input('What number you think he thought? '))

  if whatIthink == whatTheComputerThink:
    print('WOW! You hit it!')
    print('You need {} tries to win.'.format(tries))
    userWin = True

  else:
    print("That's a shame. He thought the number {}. Maybe in another time you can do it right.".format(whatTheComputerThink))
    tries += 1