# write a python program to sum three given integers.However, if two or more values are equal sum will be zero.
a = int(input("enter a first number"))
b = int(input("enter a second number"))
c = int(input("enter a third number"))
if a==b==c or a==b or a==c:
    print("the sum is 0")
else:
    print(f"the sum of three number is{a+b+c}")