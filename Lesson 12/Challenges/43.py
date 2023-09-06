userHeight = float(input("What's your height (in cm)? "))
userWeight = float(input("What's your weight? "))

userIMC = (userWeight) / ((userHeight/100)**2)

if userIMC <= 18.5:
  print("You are underweight!")

elif 18.5 < userIMC <= 25:
  print("You are in the ideal weight!")

elif 25 < userIMC <= 30:
  print("You are overweight!")

elif 30 < userIMC <= 40:
  print("You are obese!")
  
elif userIMC > 40:
  print("You are with morbid obesity!")