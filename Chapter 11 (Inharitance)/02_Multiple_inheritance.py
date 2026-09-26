class employee:
    def __init__(delf):
        print("Constructor of Employee")
    e=1

class programmer:
    def __init__(self):
        print("Constructor of programmer")
    p=2

class coder(employee, programmer):
    def __init__(self):
        print("Constructor of coder")
    c=3

a = employee()
print(a.e)
b = programmer()
print(b.p)
m = coder()
print(m.e , m.p, m.c)
