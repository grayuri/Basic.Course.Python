salaryLimit = 1250
minDiscount = 10 / 100
maxDiscount = 15 / 100

crudeUserSalary = float(input("What's your actual salary? "))

userIncreasedSalary = 0

if crudeUserSalary <= 1250:
  userIncreasedSalary = crudeUserSalary + (crudeUserSalary * minDiscount)
else:
  userIncreasedSalary = crudeUserSalary + (crudeUserSalary * maxDiscount)

increasedValue = userIncreasedSalary - crudeUserSalary

print("So, your salary with an increase is $ {:.2f}".format(userIncreasedSalary))
print("If you want to know, the value increased with an discount was $ {:.2f}".format(increasedValue))