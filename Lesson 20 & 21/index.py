def setDouble(list):
  for i in range(0, len(list)): list[i] *= 2

list = [1,2,3,4,5]

print(list)
setDouble(list) # Calling
print(list)

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-= |

def setLoop(i, f, p):
  for index in range(i, f, p): print(index)

setLoop(0, 20, 2)