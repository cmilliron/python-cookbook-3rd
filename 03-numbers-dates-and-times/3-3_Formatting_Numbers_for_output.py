'''
3.3 Formatting Numbers for Output

Problem
You need to format a number for output, controlling thenumbers of digits,
alinement, inclusion of thousand separator, and other details

Solution
format()

'''

x = 1234.567890

print(format(x, "0.2f"))
print(format(x, ">10.1f"))
print(format(x, "<10.1f"))
print(format(x, "^10.1f"))
print(format(x, ","))
print(format(x, "0,.1f"))
print(format(x, "e"))
print(format(x, "0.2E"))

print('The value is {:0,.2f}'.format(x))
