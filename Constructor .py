class EMP:


    def __int__(self,x,y,z,a):
        self.name=x
        self.lastname=y
        self.age=z
        self.salary=a


    def show(self):
        print("rrr",self.name)
        print("hhhh",self.lastname)
        print("mmmmm",self.age)
        print("nnnn",self.salary)



name=input("enter the name ")
lastname=input("enter the lastname")
age=int(input("enter the age"))
salary=int(input("enter the salary"))

k=EMP(name,lastname,age,salary)

