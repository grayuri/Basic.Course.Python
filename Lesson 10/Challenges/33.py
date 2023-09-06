a = 1
b = 5
c = 0

higherNumber = 0
lowestNumber = 0

if a > b > c:
  higherNumber = a
  lowestNumber = c
if b > a > c:
  higherNumber = b
  lowestNumber = c
if c > b > a:
  higherNumber = c
  lowestNumber = a
if a > c > b:
  higherNumber = a
  lowestNumber = b
if c > a > b:
  higherNumber = c
  lowestNumber = b
if b > c > a:
  higherNumber = b
  lowestNumber = c

print("The heighest number is {} and the lowest is {}".format(higherNumber, lowestNumber))