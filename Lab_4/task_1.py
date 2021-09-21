import math

n = int(input('Enter n:'))

S = 0

for num in range(1, n):
    S += math.sin(num)

print(1/S)