player = dict()

player['name'] = input('Name of the Player: ')
player['gols'] = []
player['total'] = 0
quantityOfMatches = int(input(f"How many matches {player['name']} play? "))

for i in range(0, quantityOfMatches):
  gols = int(input(f"How many gols {player['name']} done in the {i + 1}o. match? "))
  player['gols'].append(gols)
  player['total'] += gols

print()
print("="*60)
print(player)

print()
print("="*60)
for field, value in player.items():
  print(f"The field {field} have the value {value}")

print()
print("="*60)
print(f"{player['name']} plays {quantityOfMatches} matches.")
for index, value in enumerate(player['gols']):
  print(f"  - In the {index + 1}, {player['name']} done {value} gols.")
print(f"The total of gols that {player['name']} done was {player['total']}.")