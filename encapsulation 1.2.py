class EMP:
    __salary=5000

    def getsalary(self):          #...getter only return
        return self.__salary

    def setsalary(self,m):       #....setter...new value will be set
        self.__salary=m


k=EMP()
k.setsalary(20000)              #..we will given new value with setter
print(k.getsalary())            #...we will check our new value set
