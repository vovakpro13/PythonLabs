str = input('Your text: ').replace(" ", "")

letters = {}

for letter in str:
    if letter in letters:
        letters[letter] += 1
    else:
        letters[letter] = 1

maxLetter = ''
maxCount = 0

for item in letters.items():
    if maxCount < item[1]:
        maxCount = item[1]
        maxLetter = item[0]

print(maxLetter, maxCount)
