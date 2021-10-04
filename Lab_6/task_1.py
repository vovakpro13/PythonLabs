from modules import task_1
from modules import task_2

x = int(input('Enter x: '))
y = int(input('Enter y: '))
z = int(input('Enter z: '))


b = task_1.get_b(x, y, z)
a = task_1.get_a(x, y, z, b)

print('b = ', b)
print('a = ', a)

array = [1, 3, 2]
print('Array: ', array)
print('Max from array: ', task_2.find_max(array, array[0]))