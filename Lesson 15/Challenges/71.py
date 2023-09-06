import math

money = 1234

cedulesOf50 = math.floor(money / 50)
quantityOf50 = cedulesOf50 * 50

cedulesOf20 = math.floor((money - quantityOf50) / 20)
quantityOf20 = cedulesOf20 * 20

cedulesOf10 = math.floor(((money - (quantityOf50 + quantityOf20)) / 10))
quantityOf10 = cedulesOf10 * 10

cedulesOf1 = math.floor(money - (quantityOf50 + quantityOf20 + quantityOf10))

print(cedulesOf1)