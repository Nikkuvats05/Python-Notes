class employee():
    lang = "py"
    salery = 1200000

    def getinfo(self):
        print(f"lang is {self.lang} and salery is {self.salery}")

    def greet(self):
        print("Good morning")
   
Nikhil = employee()
Nikhil.lang = "Cpp"

Nikhil.greet()
Nikhil.getinfo() # It is same as (Employee.getinfo(Nikhil))
