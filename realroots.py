import math

aval = float(input("Please enter the value of a : "))
bval = float(input("Please enter the value of b : "))
cval = float(input("Please enter the value of c : "))
zero1 = (-bval + math.sqrt(bval**2 - aval*cval*4))/(2*aval)

if zero1 == 0:
    print("There are 1 roots")
elif zero1 < 0:
    print("There are no roots")
elif zero1 > 0:
    zero2 = (-bval - math.sqrt(bval**2 - aval*cval*4))/2*aval
    print("There are 2 zeros, " + str(zero1) + "and " + str(zero2))