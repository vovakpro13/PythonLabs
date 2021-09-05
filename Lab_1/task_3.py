# variant 8

print('Hi there, let\'s do our third task! (Three-digit number.)')


def get_number():
    number = input('Enter the three-digit number (123, 753, 009...): ')

    if len(number) > 3:
        print('Ooops, you entered so long number 😕 \nTry again)\n')
        return get_number()

    if len(number) < 3:
        print('Ooops, you entered so short number 😕 \nTry again)\n')
        return get_number()

    return number


def get_sum(string):
    summary = 0

    for i in [0, 1, 2]:
        summary += int(string[i])

    return str(summary)


result = get_sum(get_number())

print('Ok, the sum of digits equals to ' + result)
