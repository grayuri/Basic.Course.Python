height = float(input("What's the wall's height? "))
width = float(input("What's the wall's width? "))
wallsArea = height * width
literPerM2 = 2
necessaryLiters = wallsArea / literPerM2

print("So you will need {} liters of paint to do this service.".format(necessaryLiters))