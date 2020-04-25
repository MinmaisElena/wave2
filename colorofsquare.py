position = str(input("Enter the position of square as alphabet : "))
position2 = str(input("Enter the position of square as number : "))
if position == str("a") or str("c") or str("e") or str("g") and position2 % 2 == 0:
    print("The square is white.")
elif position == str("a") or str("c") or str("e") or str("g") and position2 % 2 == 1:
    print("The square is black")
elif position == str("b") or str("d") or str("f") or str("h") and position % 2 == 0:
    print("The square is black")
elif position == str("b") or str("d") or str("f") or str("h") and position % 2 == 1:
    print("The square is white.")
else:
    print("Please check your spelling")