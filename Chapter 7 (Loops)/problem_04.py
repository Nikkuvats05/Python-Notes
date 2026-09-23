# Find factorial

n = int(input("enter the no = "))

p = 1
for i in range (1, n+1):
    p = p*i

print(f"factorial of {n} is = {p}")