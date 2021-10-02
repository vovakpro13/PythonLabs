from math import factorial, sin, sqrt, cos


def get_b(x, y, z):
    return (abs(x + y)**0.2 / abs(z)**1.34) + \
           ((y - z)**2 / (1 + sin(y)**2)) + \
           (abs(z - y)**3 / (1 - cos(x**2)))


def get_a(x, y, z, b):
    return (sqrt(abs(x**2 - 1)**0.3) - abs(y + 2*b)**1./3) / \
           (1 + x + (y**2 / factorial(2)) + (z**3 / factorial(3)))