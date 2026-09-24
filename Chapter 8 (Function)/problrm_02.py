# FARNITE TO CELCIUS    C/5 = (f-32)/9

def FtoC(n):
    return 5*(n-32)/9

f = int(input("Enter temp in farnite = "))
print(FtoC(f))