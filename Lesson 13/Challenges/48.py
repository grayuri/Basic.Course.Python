total = 0

for c in range(1, 500 + 1):
  if (c % 3 == 0):
    total += c

print("The final value of multiples of 3 in a range of 500 elements is {}.".format(total))