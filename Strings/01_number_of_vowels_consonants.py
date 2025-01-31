# Write a program that counts the number of vowels and consonants in a string.
s = "Hello How are You? Today is amazing"
vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
vowel_count, cons_count = 0, 0
for i in s:
    if (ord(i) in  range(ord('a'), ord('z') + 1)) or (ord(i) in range(ord('A'), ord('Z') + 1)):
        if i in vowels:
            vowel_count += 1
        else:
            cons_count += 1
            
print(f"vowels: {vowel_count}\nconsonants: {cons_count}")