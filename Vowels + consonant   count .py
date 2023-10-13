count_consonant=0
count_vowels=0
user=input("enter the paragraph")
vowels=['a','e','i','o','u']
for i in user:
    for j in i:
        if (j in vowels):
            count_vowels+=1

    else:
        count_consonant+=1
print(count_consonant,"count of consonant")
print(count_vowels,"count of vowels")
