n = int(input('Enter n:'))

S = 0
P = 1

for k in range(1, n):
    S += pow(2, k) / pow(k, 2)
    P *= pow(2, k) / pow(k, 2)

print('S = ', S)
print('P = ', P)

