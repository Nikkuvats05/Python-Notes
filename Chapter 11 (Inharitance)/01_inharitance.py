class employee:
    company = "ITC"

    def show(self):
        print(f"Name is {self.name} and alery is : {self.salery}")

class programmer(employee):
    company ="Info tech"

    def showlang(self):
        print(f"Name is {self.name} and he is comfortacle in {self.lanf} language")


a = employee()
b = programmer()

print(a.company, b.company)