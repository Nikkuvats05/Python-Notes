# Find if no is prime or not

n = int(input("Enter the no = "))

for i in range (2,n-1):
    if(n%i == 0):
        print("not prime")
        break
else:
    print("no is prime")