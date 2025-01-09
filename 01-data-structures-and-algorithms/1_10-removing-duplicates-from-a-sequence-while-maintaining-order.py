def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1,2,5,1,2,6,8,4,8,9,5,1,5,9,5,3,1]

print(list(dedupe(a)))