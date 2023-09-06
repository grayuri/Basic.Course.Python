people = dict()

people['name'] = input("Name: ")
people['birth'] = int(input("Year of birth: "))
people['ctps'] = int(input("CTPS (0 if you don't have): "))

haveCtps = False

if (people['ctps'] != 0):
  haveCtps = True
  people['hiring'] = int(input("Year of your hiring: "))
  people['salary'] = float(input("Salary: "))
  yearOfRetirement = (people['hiring'] + 35) - people['birth']
  people['retirement'] = yearOfRetirement

print()
print("peopleal Informations: ")
print(f"- Name: {people['name']}")
print(f"- Birth: {people['birth']}")
print(f"- CTPS: {people['ctps']}")

if (haveCtps == True):
  print(f"- Hiring: {people['hiring']}")
  print(f"- Salary: $ {people['salary']:.2f}")
  print(f"- Retirement: {people['retirement']}")