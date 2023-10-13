class Emp:

    def __init__(self,x,y,z,a,b,c):
       self.name=x    # ATTRIBUTES
       self.age=y
       self.salary=z
       self.dep=a
       self.blood=b
       self.id=c





ob=Emp("rahul",29,75000,"sdm","o","A1552")
ob2=Emp("Tarun",35,2500,"ips","ab-","B1256")


print(ob.__dict__)
print(ob2.__dict__)




