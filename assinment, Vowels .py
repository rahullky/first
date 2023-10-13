k=['hello','ducat','my','rhthm','gaurav','try','sky']
g=['a','i','o','u','e']
n=[]
for i in k:
    for j in  i:
        if(j in g):
            break

    else:
        n.append(i)
print(n)