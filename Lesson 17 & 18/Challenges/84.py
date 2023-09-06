totalPeople = 0
highestWeight = -999
peopleWithHighestWeight = []
lowestWeight = 999
peopleWithLowestWeight = []
finishProgram = False

while not finishProgram:
  name = input("What's the name of the person? ")
  weight = float(input(f"What's the weight of {name}? "))

  if weight > highestWeight:
    peopleWithHighestWeight[:] = []
    highestWeight = weight
  
  if weight < lowestWeight:
    peopleWithLowestWeight[:] = []
    lowestWeight = weight
  
  if weight == highestWeight:
    peopleWithHighestWeight.append(name)
  
  if weight == lowestWeight:
    peopleWithLowestWeight.append(name)

  totalPeople += 1

  print()
  choice = input("Do you want begin? [Y]es or [N]ot: ").lower()
  print()

  if choice == "n":
    finishProgram = True
  else:
    finishProgram = False

print(f"The total amount registed is {totalPeople}")
print(f"The highest weight registered is {highestWeight} Kg. It's the weight of {peopleWithHighestWeight}")
print(f"The lowest weight registered is {lowestWeight} Kg. It's the weight of {peopleWithLowestWeight}")