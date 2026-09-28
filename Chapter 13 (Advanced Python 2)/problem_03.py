# Make a fxn which fiulter the no which are divisible by 5 only?
def div5(n):
    if(n%5 == 0):
        return True
    return False

l = [5,565,333,5,5,6455,5786,90,67780,665690,6655,7655,56,7880,45]

f = list(filter(div5, l))
print(f)