
class Emp:
    def __int__(self,x,y,z,a):
        self.name=x
        self.lastname=y
        self.age=z
        self.salary=a

    def show(self):
        print("Emp name is ",self.name)
        print("Emp  lastname ",self.lastname)
        print("Emp salary is ",self.salary)
        print("Emp age is ",self.age)


Name=input("enter the name")
last=input("enter the lastname")
salary=input("enter the salary")
age=input("enter the age")


k=Emp(Name,last,salary,age)
k.show()




