'''
3.2 Performing Accurate Decimal Calculations

Problem
You need to perform accurate calculations with deciaml numbers, 
and don't want the samll erros that naturally occur with floats

Solutions
A well-known issue with floating-point numbers is that they can't accurately
represent all based-10 decimals.
'''

a = 4.2
b = 2.1
print(a + b)
print(a + b == 6.3)

from decimal import Decimal
c = Decimal('4.2')
d = Decimal("2.1")
print(c + d)
print(type (c + d))
print((c + d) == Decimal('6.3'))

from decimal import localcontext
e = Decimal('1.3')
f = Decimal("1.7")
print(e / f)

with localcontext() as ctx:
    ctx.prec = 3
    print(e / f)

with localcontext() as ctx:
    ctx.prec = 50
    print(e / f)

nums = [1.23e+18, 1, -1.23e+18]
print(sum(nums))

total = 0.0
for n in nums:
    print(f"number: {n}")
    total += n
    print(f"Total: {total}")

import math
print(math.fsum(nums))