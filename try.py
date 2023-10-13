def smartbill(fun):
    def inner (u,r):
        if(u<=200):
            u=0
        elif(u>=200):
            u=-200
        return fun(u,r)
    return inner




@smartbill
def ebills(u,r):
     z=u*r
     print(z)





ebills(200,12)