# a student will not be allowed to sit in exam if his/her attendance is les than 75%.
# take following input from users
# number of class held
# number of class attended and print percentage of class attended.is student allowed to sit in exam or not.
a = int(input("enter a number of class held "))
b = int(input("enter a number of class attended"))
percentage = b/a*100
if percentage>75:
    print("students are allowed to sit in exam")
else:
    print("students are not allowed to sit in exam")

