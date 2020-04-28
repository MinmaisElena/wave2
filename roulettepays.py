import random

num = random.randint(0,36)
print("The spin resulted in " + str(num) + "...")
if num == 0:
    print("Pay 0")
elif num != 0:
    print("Pay " + str(num))
    if num < 19:
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")

    if num == 1 or 3 or 7 or 9 or 12 or 14 or 16 or 18 or 19 or 21 or 23 or 25 or 27 or 30 or 32 or 34 or 36:
        print("Pay red")
    else:
        print("Pay black")

    if num%2 == 1:
        print("Pay odd")
    elif num%2 == 0:
        print("Pay even")

    