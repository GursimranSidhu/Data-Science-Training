# s1=input("Enter any string: ")
# s1=s1.lower()
# count_vowel=0
# count_const=0
# vowels=("a","e","i","o","u")
# for char in s1:
#     if char in vowels:
#         count_vowel+=1
#     else:
#         count_const+=1
# print(count_vowel)
# print(count_const)

def vowel(s):
    s=s.lower()
    count_vowel=0       
    count_consonant=0   
    vowels={"a","e","i","o","u"}       
    for char in s:
        if char in vowels:
            count_vowel+=1        
        else:
            count_consonant+=1     
    print("Vowels: ",count_vowel)
    print("Consonants: ",count_consonant)

vowel("pythonlobby")
vowel("sabudhfoundation")