#HOW CAN COUNT IN STRING DATA VOWELS + CONSONANT
coun_vowel=0
count_consonant=0

user='kuntimemorialpublicschool'
vowel='AEIOUaeiou'
for i in user:
    if i in vowel:
        coun_vowel+=1
    else:
        count_consonant+=1
print('vowel',coun_vowel)
print('consonant',count_consonant)
