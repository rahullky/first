#...Inner class / Nested class also know
class Lang:
    x="python"

    def show(self):
        print("this is my programing language ",self.x)

class special(Lang):
    def show2(self):

        print("data scienctist")
        print("web devploments")
        print("python devloper")

k=Lang()
k.show()

t=special()
t.show2()