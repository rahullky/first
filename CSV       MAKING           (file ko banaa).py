import csv

i=open("d://newkk1.csv","w",newline='')
write= csv.writer(i)

write.writerow(["Sn","Name","Age"])

write.writerow([1,"Rahul",56])
write.writerow([2,"Esha",89])
write.writerow([3,"Rekh",19])
write.writerow([4,"Teena",45])
write.writerow([5,"Sonu",78])
write.writerow([6,"Arvind",35])


