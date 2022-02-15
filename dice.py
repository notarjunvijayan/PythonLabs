import random


def roll(res):
    dice = random.randint(1,7)
    return dice


print("::Roll the Dice::")
res = 0
while 1:
    prompt = int(input("Enter 1 to roll a random dice\nEnter 2 to exit: "))
    if prompt == 1:
        result = roll(res)
        print(f"Dice rolled, you got number {result}")
    elif prompt == 2:
        break
    else:
        print("Invalid Input")
