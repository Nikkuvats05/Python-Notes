# 5. Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce
l = [5,565,333,5,5,6455,5786,90,67780,665690,6655,7655,56,7880,45]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater, l))