import math     
# 1)
degree = float(input("Input degree: "))
rad = degree * (math.pi/180)
print(f'Output radian: {round(rad, 6)}')

print("-" * 30)

# 2)
h = float(input('Height: '))
a = float(input('Base, first value: '))
b = float(input('Base, second value: '))
area = (a + b)/2 * h
print(f'Expected Output: {area}')

print("-" * 30)

# # 3)
n = int(input("Input number of sides: "))
a = int(input("Input length of a side: "))
area = (n * a**2)/4 * math.tan(math.pi/n)
print(f'The area of the polygon is: {round(area)}')

print('-' * 30)

# 4)
a = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))
area = a * h
print(f'Expected Output: {area}')


