# variant 8

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


print('Hi there, let\'s do our fourth task! (Points on graph)')

x = int(input('Enter the x : '))

print('Good!')

y = int(input('Enter the y : '))

point = Point(x, y)


def check_point(p):
    return (p.x >= 1) and (p.y >= 2) and (p.y <= 4)


print(
    '\nAlmost Done! \n\nPoint (x: ' + str(x) + ', y: ' + str(y) + ') ' +
    ('belongs to' if check_point(point) else 'not belongs to') + ' the area!'
)
