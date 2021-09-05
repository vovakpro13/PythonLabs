# variant 8
import math

print('Hi there, let\'s do our second task! (Perimeter, Diagonal length)')

length = int(input('Enter the length of the rectangle: '))

print('Good!')

width = int(input('Enter the width of the rectangle: '))

perimeter = length * width
diagonal = math.sqrt(length ** 2 + width ** 2)

print('\nAlmost Done! \n\nThe perimeter equals to ' + str(perimeter) + '\nThe diagonal equals to ' + str(diagonal))
