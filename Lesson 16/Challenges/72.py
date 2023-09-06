tuple = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
userNumber = -1

while userNumber not in tuple:
  userNumber = float(input("Type a number between 0 and 20: "))

print(f"Very good! You typed {userNumber}")