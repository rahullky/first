class Emp:

    def __init__(self):
       self.name="Raj"       # ATTRIBUTES
       self.age=25
       self.salary=75000
       self.dep="Finance"



ob=Emp()
print(ob.__dict__)
