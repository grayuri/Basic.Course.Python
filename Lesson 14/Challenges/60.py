number = int(input("What number do you want to know the factorial? "))
firstNumberValue = number
factorial = 1

while(number > 1):
  factorial = factorial * number
  number -= 1

print("The factorial of {} is {}".format(firstNumberValue, factorial))