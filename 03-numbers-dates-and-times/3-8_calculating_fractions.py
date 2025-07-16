from fractions import Fraction

a = Fraction(5, 4)
b = Fraction(7, 16)

print(a + b)

print(a * b)

c = a * b

print(str(c.numerator) + " / " + str(c.denominator))

print(float(c))

# Limitign the denominator of a value

print(c.limit_denominator(8))

# Converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)
