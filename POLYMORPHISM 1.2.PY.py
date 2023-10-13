"""......OVERLODING METHOD........"""
"""WE can run one parameter  With NONE"""
"""we can run TWO parameter   with NONE """
"""WE CAN also more than parameter   """

class vip():
    def vsp(self,x=None,y=None):
        if x!=None and y!=None:
            print(x+y)

        elif x!=None:
            print(x*x)


        else:
            print("please something else")

t=vip()
t.vsp(5,5)





