""".....Overriding method....."""



class A:
    def laptop(self):
        print("Laptop have is old version")


class B(A):
    def laptop(self):
        print("but now we have availble latest version ")



h=B()
h.laptop()

