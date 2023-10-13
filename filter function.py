# salary find out >20000   1.1

k=[2000,10000,40000,50000,60000,70000]
for i in k:
    if(i>10000 and i<50000):
     print(i)


# WITH LAMBDA USE 
k=[20000,10000,40000,50000,45000,48000,60000,70000]
s=list(filter(lambda x:x>40000 and x<70000,k))
print(s)



# MAP   WITH SALARY  FIND OUT   (TRUE FALSE)

k2=[2000,10000,40000,50000,45000,48000,60000,70000]
s=list(map(lambda x:x>40000 and x<70000,k))
print(s)

# WE WILL COUNT THE TRUE VALUE 
K2=s.count(true)
print(k2)