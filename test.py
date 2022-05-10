
vowels = ["a", "e", "i", "o", "u"]
sentence = "aaexioummmdidd"

number_of_vowels = 0
for i in vowels:
    number_of_vowels += sentence.count(i)


print(number_of_vowels)