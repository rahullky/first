import functools

k=["hello','how','are','you','ducat"]


f=functools.reduce(lambda x,y:x+y,k)
print(f)