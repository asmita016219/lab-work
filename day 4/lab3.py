# ask user to enter age,gender(M or F) and then using following rules print their place of service.
# if employee is female, then she will work only in urban areas.
# if employee is a male and age is between 20 to 40 then he may work in anywhere
# if employee is male and age is between 40 to 60 then he will work in urban areas only
# any other input of age should print 'ERROR'.
print("enter age")
age =int(input())
print ("gender?(M or F)")
gender = input()
if (gender =="F" or gender =="f") and 20<=age<=60:
    print("work only in urban areas")
elif (gender =="M" or gender =="m") and 20<age<40:
    print("works anywhere")
elif (gender =="M" or gender =="m") and 40<=age<60:
    print("work only in urban areas")
else:
    print("ERROR")
