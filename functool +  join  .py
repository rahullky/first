k=['raj','kumar','singh']

t=''.join(k)

print(t)

print()

import functools

m=['ashish','kumar','arav']

a=functools.reduce(lambda x,y:x+" "+y,m)

print(a)