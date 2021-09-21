import random

n = int(input('Enter n:'))

a = []
b = []
c = []

for i in range(n):
    a.append(random.random())
    b.append(random.randint(-10, 10))
    c.append(random.randint(0, 50))

S = 0

for num in c:
    if not num % 2 == 0:
        S += num

print('a = ', a)
print('b = ', b)
print('c = ', c)

print('Sum c = ', S)