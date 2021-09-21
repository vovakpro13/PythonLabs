# variant 8

x = int(input('Enter x:'))
a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = int(input('Enter c:'))

if a <= x <= b:
    print((x - a) / (b - a))

elif b <= x <= c:
    print((c - x) / (c - b))

elif x <= a or c <= x:
    print(0)

