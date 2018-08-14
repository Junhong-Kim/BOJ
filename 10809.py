from string import ascii_lowercase

word = input()
alphabets = list(ascii_lowercase)

result = ['-1'] * len(ascii_lowercase)
for index, alphabet in enumerate(alphabets):
    if alphabet in word:
        result[index] = str(word.find(alphabet))

print(' '.join(result))
