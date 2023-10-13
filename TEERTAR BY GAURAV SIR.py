w = "ducat is very good ducat instuition but ducat is very low score .ducat is high noida"

r=w.split()

l=[]
k=[]


for i in r:
    if i=='is':
        l.append(i)

    elif i=='score':
        l.append(i)


    else:
        k.append(i)

print(l)
print(k)