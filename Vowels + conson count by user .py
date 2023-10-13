coun_vowels=0
coun_consonat=0
user=input("enter the aphabates")
vowels='AEIOUaeiou'
for i in user:
    if i in vowels:
        coun_vowels+=1
    else:
        coun_consonat+=1
print('count vowels',coun_vowels)
print('count consonat',coun_consonat)

