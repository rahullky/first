class A :
    def displayA(self):  #FATHER  ---PROPERTY--> CHILD
        print("WELCOME TO  CUBE TECH :A ")


class B(A):  # WE WILL ADD CLASS A
    def displayB(self):
        print("GOOD BYE PERSON  :B  ")




objt=B()
objt.displayA()
objt.displayB()



