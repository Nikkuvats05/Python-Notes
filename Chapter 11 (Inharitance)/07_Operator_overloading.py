class number:
    def __init__(self, n):
        self.n = n

    def __add__(self, num):    #Direct '+' operator kam nhi krta classes me ye fxn banana jruri h and aisi hi subtract, multipy, divide ke liye hoya h
        return self.n + num.n

n = number(1)
m = number(2)

print(n + m)

# p1-p2 # p1.sub_(p2)
# p1*p2 # p1.mul_(p2)
# p1/p2 # p1. truediv_(p2)
# p1//p2 # p1._ floordiv_(p2)