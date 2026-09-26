# Create a Class "Programmer" for storing information of few programmers working at Microsoft.

class programmer:
    company = "Microsoft"

    def __init__(self, name, salery, pincode):
        self.name = name
        self.salery = salery
        self.pincode = pincode

    def getinfo(self):
        print(f"Name = {self.name}\nSalery = {self.salery}\nPinCode = {self.pincode}")

p = programmer("Nikhil", 1200000, 124103)
p.getinfo()

p = programmer("Rohan", 1200000, 124100)
p.getinfo()