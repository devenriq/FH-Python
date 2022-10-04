vowels = ["a", 'e', 'i', 'o', 'u']
found = []
word = input('Provide a word to play with: ')


for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)
