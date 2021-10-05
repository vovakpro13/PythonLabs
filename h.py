# # 4.1
#
# c = int(input('enter the  number: '))
#
# sum = 0
#
# for n in range(1, c):
#     sum += -1**(n + 1) / (n * (n + 1))
#
# print(sum)
#
# # 4.2
#
# import random
#
# n = int(input('enter n:'))
#
# a = []
# b = []
# v = []
#
# for i in range(n):
#     a.append(random.random())
#     b.append(random.randint(-10, 10))
#     v.append(random.randint(0, 50))
#
# # перевіряємо чи в масиві всі елементи розташовані в порядку спадання
# i = 1
# isSorted = True
#
# while i < len(b):
#     if b[i] > b[i-1]:
#         isSorted = False
#         break
#
#     i += 1
#
# if isSorted: # якшо да - то просто його виводимо
#     print(b)
# else:  #якшо нє - то шукаємо всі від'ємні елементи і міняємо їх на 1
#     i = 0
#     while i < len(b):
#         if b[i] < 0:
#             b[i] = 1
#         i += 1
#     print(b)

# 5.1

import random

rows = int(input('Enter rows count:'))
cols = int(input('Enter cols count:'))

a = []
b = []
c = []
g = []

for x in range(rows):
    a_row = []
    b_row = []
    c_row = []
    g_row = []
    for y in range(cols):
        a_row.append(random.random())
        b_row.append(random.randint(-10, 10))
        c_row.append(random.randint(0, 20))
        g_row.append(random.uniform(-10, 10))
    a.append(a_row)
    b.append(b_row)
    c.append(c_row)
    g.append(g_row)

min_col_index = 0
min = 21

for row in range(rows):
    for col in range(cols):
        print(c[row][col], end='   ')
        if min >= c[row][col]:
            min = c[row][col]
            min_col_index = col
    print()

print('--------------------------')
print('min col:', min_col_index)
print('--------------------------')


for row in range(rows):
    val = c[row][0]
    c[row][0]  = c[row][min_col_index]
    c[row][min_col_index] = val

for row in range(rows):
    for col in range(cols):
        print(c[row][col], end='   ')
    print()

# 5.2

times = [
    { "hours": 4, "minutes": 10 },
    { "hours": 4, "minutes": 8 },
    { "hours": 23, "minutes": 9 },
    { "hours": 18, "minutes": 42 },
    { "hours": 21, "minutes": 59 },
    { "hours": 11, "minutes": 37 },
    { "hours": 23, "minutes": 21 },
]

first_time_index = int(input('Enter first time index: '))
second_time_index = int(input('Enter second time index: '))

t1 = times[first_time_index]
t2 = times[second_time_index]

if t1.get('hours') < t2.get('hours') or (t1.get('hours') == t2.get('hours') and t1.get('minutes') < t2.get('minutes')):
    print('Time ' + str(times[first_time_index]) + ' was earlier')
else:
    print('Time ' + str(times[second_time_index]) + ' was earlier')
