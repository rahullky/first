#.....list..with..string..ko chota kar do....

import functools

k=['hello','how','are','you','india']

t=functools.reduce(lambda x,y:x+" "+y,k)
print(t)



r = ['tarun','is','good','person']
m="  ".join(r)

print(m)