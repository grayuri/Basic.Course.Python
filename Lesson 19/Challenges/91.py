from random import randint

players = []
quantityOfPlayers = 4

winner = ''
highestNumber = -999

for i in range(0, quantityOfPlayers):
  player = dict()

  player['name'] = input("What's the name of the player? ")
  player['number'] = randint(1,10)

  if (player['number'] > highestNumber):
    winner = player['name']
    highestNumber = player['number']

  players.append(player.copy())

print()
print("The players are: ")

for i in range(0, len(players)):
  print(f"- {players[i]['name']}: {players[i]['number']}")

print()
print(f"The winner is {winner}, with {highestNumber} points.")