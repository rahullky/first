# salary se realative questions $   dollar we have to dollar remove in this data list

k=['12,789$','785,78$','521,12$']
l=[]
for i in k:
    m=""
    for j in i:
        if(j.isdigit()):
            m=m+j

    l.append(m)
    print(l)