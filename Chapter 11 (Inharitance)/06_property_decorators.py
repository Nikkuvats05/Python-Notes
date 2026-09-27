class employee():
    a = 1

    @classmethod
    def show(cls):
        print(f"The class attribute of a is = {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"

    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]


e = employee()

e.name = "Nikku Sharma"

print(e.name)            #Both will return the same string or name line 22 == line23
print(e.fname, e.lname)