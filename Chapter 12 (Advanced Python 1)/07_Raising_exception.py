a = int(input("Enter a number = "))
b = int(input("Enter a number = "))

if(b == 0):
    raise ZeroDivisionError("Hey our program is not meant to divide number by zero")   #Janbujkr error create kiya h taki developer ko galti krti h pta lag jay

else:
    print(f"Division of a/b is = {a/b}")