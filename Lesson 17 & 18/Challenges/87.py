matrix = [[0,0,0], [0,0,0], [0,0,0]]

pairSum = 0
thirdColumnSum = 0
highestValueOfSecondColumn = -999

for row in range(0, len(matrix)):
    for col in range(0, len(matrix[row])):
        number = int(input("Type a number: "))
        matrix[row][col] = number

        if col == 2:
            thirdColumnSum += number
        
        if number % 2 == 0:
            pairSum += number
        
        if row == 1:
            if number > highestValueOfSecondColumn:
                highestValueOfSecondColumn = number

for row in range(0, len(matrix)):
    for col in range(0, len(matrix[row])):
        if col == 2:
            print(f"[{matrix[row][col]}]")
        else:       
            print(f"[{matrix[row][col]}]", end="")

print(f"The sum of the pair number is {pairSum}")
print(f"The sum of the values of the third column is {thirdColumnSum}")
print(f"The highest number in the second line is {highestValueOfSecondColumn}")