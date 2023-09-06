velocityLimit = 80

print("The velocity limit in the roads is {} KM.".format(velocityLimit))

userVelocity = float(input("What was your velocity right there? "))

taxPerKm = 7

userTax = 0

velocityTrespassed = 0

if userVelocity > velocityLimit:
  velocityTrespassed = userVelocity - velocityLimit
  userTax = velocityTrespassed * taxPerKm

  print("Wow! This is to much!")
  print("Unfortunately, you have to pay $ {:.2f} of tax.".format(userTax))
else:
  print("Very fine, friend! You can go.")