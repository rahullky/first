#union me data merge hota hai
# unique data output deta hai..


s={1,2,3,2,5,1,"rahul","rahul","kumar",783,"kumar"}
s2={1,2,3,2,5,1,"rahul","rahul",784,"kumar","kumar","sonu"}

print(s.union(s2))



# set ke in dono data  me kya differnece hai?
s={1,2,3,2,5,1,"rahul","rahul","kumar",783,"kumar"}
s2={1,2,3,2,5,1,"rahul","rahul",784,"kumar","kumar","sonu"}
print(s.difference(s2))




#s.symmetric_difference() yeh dono  set me  kya unique hai

s={1,2,3,2,5,1,"rahul","rahul","kumar",783,"kumar"}
s2={1,2,3,2,5,1,"rahul","rahul",784,"kumar","kumar","sonu"}
print(s2.symmetric_difference(s))
