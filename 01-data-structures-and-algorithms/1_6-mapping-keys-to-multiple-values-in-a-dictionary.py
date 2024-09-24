"""
Problem

You want to make a dictionary that maps keys to more than one value (a so-called 'multidict').
"""

from collections import defaultdict

d_sets = defaultdict(list)
d_sets['a'].append(1)
d_sets['a'].append(2)
d_sets['b'].append(4)

d_dict = defaultdict(set)
d_dict['a'].add(1)
d_dict['a'].add(2)
d_dict['b'].add(4)

print(d_sets)
print(d_dict)

"""
Save a person from the following:
d = {}
for key, value in pairs:
    if key not in d:
         d[key] = []
    d[key].append(value)
    
Instead:
d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
"""