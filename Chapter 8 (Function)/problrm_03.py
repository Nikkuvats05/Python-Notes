# Sum of 1st n natural no

def sum(n):
    if(n==1):
        return 1
    return n+sum(n-1)

n= int(input("Enter the no = "))
sum = sum(n)
print(f"Sum from 1 to {n} is = {sum}")