# 80 Задано два слова0 Скласти програму, яка визначає, чи можна з літер
# першого з них здобути друге0 Розглянути такі варіанти: 1) повторювані
# літери другого слова можуть в першому слові не повторюватися; 2) кожна
# літера другого слова повинна входити у перше слово стільки раз, скільки
# вона входить у друге
import json

firstWord = input('Enter first word:').lower()
secondWord = input('Enter second word:').lower()

mode = int(input('Choose mode:'))


def getLetters(word):
    letters = {}

    for index in range(len(word)):
        letter = word[index]
        i = index

        while not word[slice(i, len(word))].find(letter) == -1:
            if letters.get(letter):
                letters[letter] = int(letters.get(letter)) + 1
            else:
                letters[letter] = 1
            i += len(word[slice(i, len(word))])

    return letters

if mode == 1:
    flag = True
    for letter in firstWord:
        if not letter in secondWord and flag:
            flag = False

    print(flag)

elif mode == 2:
    first = getLetters(firstWord)
    second = getLetters(secondWord)

    firstKeys = list(first)
    secondKeys = list(second)

    flag = True

    for key in firstKeys:
        if not first.get(key) <= second.get(key) and flag:
            flag = False

    print(flag)

else:
    print('Mode is not correct!')
