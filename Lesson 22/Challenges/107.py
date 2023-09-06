import Currency

price = 33
increase = 33
decrease = 33

print(f"- The half of $ {price:.2f} is $ {Currency.getHalf(price):.2f}")
print(f"- The double of $ {price:.2f} is $ {Currency.getTriple(price):.2f}")
print(f"- Increasing $ {price:.2f} by {increase}%, we have $ {Currency.getIncrease(price, increase):.2f}")
print(f"- Decreasing $ {price:.2f} by {decrease}%, we have $ {Currency.getDecrease(price, increase):.2f}")