month = str(input("Enter the month : "))
if month == str("January") or str("March") or str("May") or str("July") or str("August") or str("October") or str("December"):
    print("31 Days")
elif month == str("April") or str("June") or str("September") or str("November"):
    print("30 Days")
elif month == str("Febuary"):
    print("28 or 29 Days")
else:
    print("Please check you spelling")