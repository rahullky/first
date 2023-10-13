# (GRAND FATHER) ---PROPERTY-->(FATHER) --PROPERTY--->(SON)


class A :   # We can add pass statments
    def displayA(self):
        print("WELCOME TO  CUBE TECH :A ")

class D:
    def displayD(self):
        print("YOU ARE A DATA SCIENTIST BROTHER")


class B:
    def displayB(self):
        print("GOOD BYE PERSON  :B  ")


class C:
    def displayC(self):
        print("PYTHON DEVELEPOR PERSON:C  ")


class H(A,C,D):
    def displayH(self):
        print("data engineer person")



objt=H()
objt.displayA()
objt.displayC()
objt.displayD()





