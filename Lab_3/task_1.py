N = int(input('Enter N:'))

if 0 <= N <= 10:
    for row in range(1, N + 1):
        res = ''
        for col in range(1, row + 1):
            res += ' ' + str(N - row + col)

        print('  ' * (N - 1) + res)

    for row in range(1, N + 1):
        res = ''

        for col in range(1, row + 1):
            res += ' ' + str(row - col + 1)

        print('  ' * (N - row) + res)
else:
    print('N is not correct!')