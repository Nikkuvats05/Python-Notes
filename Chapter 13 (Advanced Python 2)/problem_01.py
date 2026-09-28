# Print a string telling name, marks and phone no of student using format fxn?

name = input("Enter yor name = ")
marks =int(input("Enter yor marks = "))
phone =int(input("Enter yor phone no = "))

a = "{} whose phone number is {} got {} marks".format(name, phone, marks)
print(a)