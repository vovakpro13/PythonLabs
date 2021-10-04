# 4.1

c = int(input('enter the  number: '))

sum = 0

for n in range(1, c):
    sum += -1**(n + 1) / (n * (n + 1))

print(sum)

# 4.2

import random

n = int(input('enter n:'))

a = []
b = []
v = []

for i in range(n):
    a.append(random.random())
    b.append(random.randint(-10, 10))
    v.append(random.randint(0, 50))

# перевіряємо чи в масиві всі елементи розташовані в порядку спадання
i = 1
isSorted = True

while i < len(b):
    if b[i] > b[i-1]:
        isSorted = False
        break

    i += 1

if isSorted: # якшо да - то просто його виводимо
    print(b)
else:  #якшо нє - то шукаємо всі від'ємні елементи і міняємо їх на 1
    i = 0
    while i < len(b):
        if b[i] < 0:
            b[i] = 1
        i += 1
    print(b)

