gender = ''

while (gender != 'M' and gender != 'F'):
  gender = input("What's your gender [M]ale/[F]emale? ").upper()
  if (gender != 'M' and gender != 'F'): 
    print("Please, insert a valid key.")