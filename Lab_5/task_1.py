import random

n = int(input('Enter n:'))
m = int(input('Enter m:'))

a = []
b = []
c = []
d = []

for x in range(m):
    a_row = []
    b_row = []
    c_row = []
    d_row = []
    for y in range(n):
        a_row.append(random.random())
        b_row.append(random.randint(-10, 10))
        c_row.append(random.randint(0, 20))
        d_row.append(random.uniform(-10, 10))
    a.append(a_row)
    b.append(b_row)
    c.append(c_row)
    d.append(d_row)

for item in b :
    print(item)

b_min = 0

for col in range(n):
    col_min = 1000000000

    for row in range(m):
        if col_min > abs(b[row][col]):
            col_min = abs(b[row][col])
    print('Min in ' + str(col) + ' col = ' + str(col_min))

    for row in range(m):
        b[row][col] = b[row][col] * col_min


for item in b:
    print(item)