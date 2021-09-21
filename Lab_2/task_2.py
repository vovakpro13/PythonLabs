# variant 8
R = 1
x = float(input('Enter x:'))
y = float(input('Enter y:'))

if x >= y and y >= -0.5:
    if (x <= 0.2 and y >= -0.5 and not pow((x - 1), 2) + pow(y, 2) <= 1) or pow((x - 1), 2) + pow(y, 2) <= 1:
        print(True)
    else:
        print(False)
else:
    print(False)