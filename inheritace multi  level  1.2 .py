# (GRAND FATHER) ---PROPERTY-->(FATHER) --PROPERTY--->(SON)


class A :
    def displayA(self):
        print("WELCOME TO  CUBE TECH :A ")


class B(A):
    def displayB(self):
        print("GOOD BYE PERSON  :B  ")


class C(B):
    def displayC(self):
        print("welcom ws cube tech :C  ")




objt=C()
objt.displayA()
objt.displayB()
objt.displayC()



