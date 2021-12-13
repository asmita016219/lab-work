# check whether the given year is leap year or not.
a = int(input("enter the year checked"))
if (a % 4 == 0 and a % 100 != 0 or a % 400 == 0):
    print("the year is a leap year")
else:
    print("the year is not a leap year")

