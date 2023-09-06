userExpression = input("Type your expression: ")

openParentesis = userExpression.count("(")
closedParentesis = userExpression.count(")")

if openParentesis == closedParentesis:
  print("Right expression!")
else:
  print("Wrong expression!")