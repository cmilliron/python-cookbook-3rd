print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.27, 1))
print(round(1.25361, 3))

#round() can be negatives to round to tens, hundreds...
a = 1627731
print(round(a, -1))
print(round(a, -2))
print(round(a, -3))

x = 1.123456
print(format(x, '0.2f'))
print(format(x, '0.3f'))
print("value is {:.03f}".format(x))

"""
Also, resist the urge to round floating-point numbers to “fix” perceived accuracy problems.
"""

a = 2.1
b = 4.2
c = a + b
print(c)

