'''
3.4 Working with Binary, Octal, and Hexadecimal Integers

Problem
You need to convert or output integers represented by binary, octal, or hexadecimal digits.

Solutions
To convert an integer into a binary, octal, or hexadecimal text string, use the 
bin(), oct(), and hex() functions
'''


x = 1234

print(bin(x))
print(oct(x))
print(hex(x))


print(format(x, "b"))
print(format(x, "o"))
print(format(x, 'x'))