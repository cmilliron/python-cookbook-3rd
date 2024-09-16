p = (4, 5)
x, y = p

print(y)
print(x)

data = [ 'ACME', 50, 91.1, (2012, 12, 21) ]

name, shares, price, date = data

print(name, shares, price, date)

# It works for Stings

s = "Hello"
a, b, c, d, e = s

print(b)

# Use throw away values for data you want to discard

_, shares, price, _ = data
print(shares, price)