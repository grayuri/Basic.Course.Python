from random import randint

quantityOfGuesses = int(input("How many guesses do you need? "))

for i in range(0, quantityOfGuesses + 1):
    list = []

    for j in range(0, 7): list.append(randint(1,60))

    print(f"- Guess {i + 1}: {list}")