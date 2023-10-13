class Emp:

    company="GOOGLE"

    def __init__(self,x,y,z):
        self.name=x
        self.age=y
        self.dep=z

    @classmethod
    def compan_new(clc):
     clc.company="TCS"
     print(f"company name is, {clc.company}")




mm=Emp("raj",25,"IAS")
Emp.compan_new()
print(mm.__dict__)

