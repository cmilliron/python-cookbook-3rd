import re
from collections import namedtuple

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

text = 'foo = 23 + 42 * 10'
master_pat = re.compile("|".join([NAME, NUM, PLUS, TIMES, EQ, WS]))

Token = namedtuple("Token", ["type", 'value'])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup(), m.group())

# Example use
for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

    ## This program doesn't work and I need to debug it. 