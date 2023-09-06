header = " List of Prices "
print("="*40)
print(f"{header:-^40}")
print("="*40)

products = ('Superframe Velka', 139.90, 'Mecanic Keyboard KDA Logitech', 720.69, 'Redragon Cobra', 118)

for index in range(0, len(products), 2):
  print(f"{products[index]:.<31}R${(products[index + 1]):>7.2f}")
print("="*40)

# Revisit this exercise after...