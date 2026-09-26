class employee():
    lang = "py"
    salery = 1200000

    def getinfo(self):
        print(f"lang is {self.lang} and salery is {self.salery}")

    @staticmethod #Agar koi fxn static h to it means it doesnot need any object and we can see also it only print string donot need any data from any object.
    def greet(self):
        print("Good morning")
   
Nikhil = employee()
Nikhil.lang = "Cpp"

Nikhil.greet()
Nikhil.getinfo() # It is same as (Employee.getinfo(Nikhil))
