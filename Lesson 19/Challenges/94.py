people = []

womenRegistered = []
ageTotal = 0
peopleAboveAgeMedia = []

finishProgram = False
while not finishProgram:
  person = dict()

  print()
  person['name'] = input("Name: ")

  validGender = False
  while not validGender:
    person['gender'] = input(f"Gender: [M / F] ").lower()

    if (person['gender'] == 'm') | (person['gender'] == 'f'): validGender = True
    else: print('Please, type a valid gender...')
  
  person['age'] = int(input(f"Age: "))

  ageTotal += person['age']

  people.append(person.copy())

  if (person['gender'] == 'f'): womenRegistered.append(person['name'])

  validChoice = False
  while not validChoice:
    print()
    choice = input(f"Do you want begin? [Y]es or [N]ot: ").lower()

    if (choice == 'y') | (choice == 'n'): 
      if (choice == 'y'): finishProgram = False
      elif (choice == 'n'): finishProgram = True
      validChoice = True
    else: print('Please, type a valid choice...')

totalGroupQuantity = len(people)
ageMedia = ageTotal / totalGroupQuantity

for i in range(0, len(people)):
  if (people[i]['age'] > ageMedia):
    peopleAboveAgeMedia.append(people[i])

print()
print("="*60)
print()
print(f"- The group have {totalGroupQuantity} people;")
print(f"- The media of the ages is {ageMedia}")
print(f"- The women registered quantity is {womenRegistered}")
print(f"- The list of the people that are above the age media:")
for i in range(0, len(peopleAboveAgeMedia)):
  print(f".Name: {peopleAboveAgeMedia[i]['name']}", end=" - ")
  print(f"Gender: {peopleAboveAgeMedia[i]['gender'].upper()}", end=" - ")
  print(f"Age: {peopleAboveAgeMedia[i]['age']}")