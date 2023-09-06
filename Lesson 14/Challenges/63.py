number = int(input("What number do you want to know the fibonacci? "))
firstNumberValue = number
fibonacci = 1
numberOne = 0
numberTwo = 1

while(number > 0):
  fibonacci = numberOne + numberTwo
  numberOne = numberTwo
  numberTwo = fibonacci
  number -= 1

print("The value the finonacci sequence of {} is {}".format(firstNumberValue, fibonacci))