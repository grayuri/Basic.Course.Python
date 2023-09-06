matrix = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]

for row in range(0, len(matrix)):
  for col in range(0, len(matrix[row])):
    matrix[row][col] = int(input("Type a number: "))

print()

for row in range(0, len(matrix)):
  for col in range(0, len(matrix[row])):
    if col == 2:
      print(f"[{matrix[row][col]}]")
    else:
      print(f"[{matrix[row][col]}]", end="")