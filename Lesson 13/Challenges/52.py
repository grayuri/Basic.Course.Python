number = int(input("Type a integer number: "))
divisible = 0

if number > 1:
  for i in range(1, number + 1):
    if number % i == 0:
      divisible += 1
  
  if (divisible == 2):
    print(number, "is prime.")
    
  else:
    print(number, "isn't prime.")
  
else:
  print("Type a number higher than 1!")