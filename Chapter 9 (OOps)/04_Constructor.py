class employee():
    lang = "py"
    salery = 1200000

    def __init__(self, name, salery, lang):  # Dunder method/fxn (starts from __ ) is called automatically
        print("I am creating an object")
        self.name = name
        self.salery = salery
        self.lang = lang


    def getinfo(self):
        print(f"Name = {self.name}\nlang is {self.lang}\nsalery is {self.salery} ")

    @staticmethod #Agar koi fxn static h to it means it doesnot need any object and we can see also it only print string donot need any data from any object.
    def greet(self):
        print("Good morning")
   
Nikhil = employee("Nikhil", 1200000, "Cpp")
Nikhil.getinfo()
