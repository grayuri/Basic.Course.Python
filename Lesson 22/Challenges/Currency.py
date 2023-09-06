def getHalf(price):
  return price / 2

def getTriple(price):
  return price * 3

def getIncrease(price, percent):
  increaseOf = percent / 100
  valueIncreased = percent * increaseOf

  return price + valueIncreased

  
def getDecrease(price, percent):
  decreaseOf = percent / 100
  valueDecreased = percent * decreaseOf

  return price - valueDecreased