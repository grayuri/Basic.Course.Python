import sys

storeName = " Super Fresh "
print("="*30)
print(f"{storeName:-^30}")
print("="*30)

finishProgram = False

total = 0
costMoreThanOneThousand = 0
mostCheapName = ""
mostCheapPrice = sys.maxsize

while finishProgram == False:
  productName = input("Product name: ")
  productPrice = float(input("Product price: $ "))

  total += productPrice

  if productPrice < mostCheapPrice:
    mostCheapName = productName
    mostCheapPrice = productPrice
  
  if productPrice >= 1000:
    costMoreThanOneThousand += 1
  
  choice = input("Do you want finish the program? [Y]es or [N]ot ")
  choice = choice.lower()
  
  if choice == "n":
    finishProgram = False
  elif choice == "y":
    finishProgram = True

footer = " End of Program "
print(f"{footer:=^30}")
print(f"The total amount was $ {total}")
print(f"You bought {costMoreThanOneThousand} products that cost more than $ 1000.00")
print(f"The most cheap product was the {mostCheapName} with $ {mostCheapPrice}")