def getFactorial(number, show=False):
  factorial = 1

  if (show == False):
    for i in range(number, 1, -1):
      factorial *= i
  else:
    for i in range(number, 1, -1):
      if (i == 2): print(i, "= ", end="")
      else: print(i, "x ", end="")

      factorial *= i
  
  print(factorial) 

getFactorial(5, True)