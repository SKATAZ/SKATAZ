a = float(input('side1: '))
b = float(input('side2: '))
c = float(input('side3: '))
s = (a + b + c) / 2 
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)