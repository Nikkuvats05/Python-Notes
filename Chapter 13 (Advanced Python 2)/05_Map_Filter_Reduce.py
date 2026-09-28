# Map = ek function ko puri list me itretate kr deta h

l = [1, 2, 3, 4, 5]

square = lambda x:x*x

sqlist = map(square, l)    # list = map(fxn name, list name)
print(list(sqlist))

# Filter example

def even(n):
    if(n%2 == 0):
        return True
    return False

onlyeven = filter(even, l)
print(list(onlyeven))

from functools import reduce

def sum(a,b):
    return a+b

mul = lambda a,b: a*b
print(reduce(sum, l)) 
print(reduce(mul, l)) 