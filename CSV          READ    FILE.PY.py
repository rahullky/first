import  csv

f=open("d://newkk1.csv","r")
s=csv.reader(f)


for i in s:
    print(i)