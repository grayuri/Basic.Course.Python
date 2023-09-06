productPrice = 1300

print("The product price is $ {:.2f}. How would you like to pay? ".format(productPrice))
print("[1] Cash")
print("[2] Cash with the card")
print("[3] 2x with the card")
print("[4] 3x or more with the card")

paymentType = int(input(''))

discount = 1
interest = 0

if paymentType == 1:
  discount = 10 / 100
  productPrice += - (productPrice * discount)

elif paymentType == 2:
  discount = 5 / 100
  productPrice += - (productPrice * discount)

elif paymentType == 3:
  productPrice

else: 
  interest = 20 / 100
  productPrice += + (productPrice * interest)

print("The final price is $ {:.2f}".format(productPrice))