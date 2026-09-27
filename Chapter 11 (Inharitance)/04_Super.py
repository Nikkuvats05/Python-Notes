class employee:
    def __init__(delf):
        print("Constructor of Employee")
    e=1

class programmer(employee):
    def __init__(self):
        print("Constructor of programmer")
    p=2

class Manager(programmer):
    def __init__(self):

        super().__init__()   #Parent class (programmer) ke init fxn ko bhi call krega

        print("Constructor of coder")
    c=3

a = employee()
print(a.e)
b = programmer()
print(b.p)
m = Manager() 
print(m.e , m.p, m.c)