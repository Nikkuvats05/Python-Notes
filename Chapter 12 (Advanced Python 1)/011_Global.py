a = 89  # Global variable can be use anywhere

def fun():
    a = 3  # Local variable can only use inside this fxn
    print(a)

# def fun2():        Ye 'global a' ko change krdega because hmne special 'global a' mention kiya h
#     global a 
#     a = 5
#     print(a)

fun()
print(a)