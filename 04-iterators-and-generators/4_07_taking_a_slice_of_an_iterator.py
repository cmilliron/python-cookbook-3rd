def count(n):
    while True:
            yield n
            n += 1

c = count(0)
# c[10:20] Will not work -> not iterable

# Now using islice()
import itertools
for x in itertools.islice(c, 10, 20):
    print(x)