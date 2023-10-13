

def cube(x):
    return x*x
print(cube(5))



def cube2(y):
    return y*y
print(cube2(2))



l=(2,4,6,8,10)

newly=list(map(cube2,l))
print(newly)

# FILTER FUNCTIONS WILL BE FILTER VALUES

def filter_function(b):
    return b>6

newly2=list(filter(filter_function,l))
print(newly2)



#WE WILL BE IMPORT     (FROM FUCTIONSTOOLS IMPORT REDUCE)
from functools import reduce

def rk(x,y):
    return x+y

l3=[5,5,5,5,2]

sum= reduce(rk,l3)
print(sum)
