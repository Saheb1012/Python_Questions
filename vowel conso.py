text = "hello mam"

vowel_count = 0
consonant_count = 0

vowels = "aeiouAEIOU"

for char in text:
    if char.isalpha():
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

result = {'vowels': vowel_count, 'consonants': consonant_count}

print(result)
