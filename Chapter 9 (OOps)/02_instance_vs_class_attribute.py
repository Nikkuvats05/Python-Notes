class employee():
    name = "Nikhil" # This is a class attribute
    lang = "py"
    salery = 1200000
    # koi bhi employee ho sbki same info print hogi but its just only an examkple of hoe does a class look.
Nikhil = employee()
Nikhil.lang = "Cpp" #Instance attribut -> Instance attribute take prefference on class attribute
print(Nikhil.name, Nikhil.lang ,Nikhil.salery)

Rohan = employee()
Rohan.name = "Rohan" #Agar ye nhi likha to iska name bhi Nikhil hi print hoga ang This a object/instance attribute
print(Rohan.name, Rohan.lang ,Rohan.salery)

