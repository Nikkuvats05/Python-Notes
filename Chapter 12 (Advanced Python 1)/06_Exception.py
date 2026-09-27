try:
    a = int(input("hey, Enter a number: "))
    print(a)
    
except ZeroDivisionError as z:
     print(z)

except Exception as e:  # Agar ye try exception na krte ti agar 'a' ke input me char dal dete to crash ho jata lekin ab crash nhi hoga,
      print(e)   # blki error print krega and continue krega agge code ko

print("Thank You")