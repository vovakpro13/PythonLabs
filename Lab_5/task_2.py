import random

db = [
    {
        'last_name': 'Попов',
        'phone_number': '+3806642342'
    },
    {
        'last_name': 'Кукурудза',
        'phone_number': '+38067686456'
    },
    {
        'last_name': 'Колос',
        'phone_number': '+380084003132'
    },
    {
        'last_name': 'Федун',
        'phone_number': '+3802332545667'
    },
]

last_name = input('Enter last name:')


def printUserData(user):
    print('Last name: ', user.get('last_name') + '\nPhone number: ' + user.get('phone_number') + '\n')


for user in db:
    if bool(last_name) and user.get('last_name').startswith(last_name):
        printUserData(user)

phone_number = input('Enter phone number: +380')

for user in db:
    if bool(phone_number) and user.get('phone_number').rstrip().replace('+380', '').startswith(phone_number):
        printUserData(user)