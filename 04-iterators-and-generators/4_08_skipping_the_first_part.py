with open("/etc/passwd") as f:
    for line in f:
        print(line, end='')

print("*" * 40)

from itertools import dropwhile
with open("/etc/passwd") as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')