s=['ravi555','gaurav888','333sonu']
k=[]
k2=[]
for i in s:
    l=" "
    p=""
    for j in i:
        if(j.isdigit()):
            l=l+j
        else:
            p=p+j
    k.append(l)
    k2.append(p)

m=dict(zip(k,k2))
print(m)
