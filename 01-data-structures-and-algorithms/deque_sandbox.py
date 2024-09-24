from collections import deque
from pprint import pprint

def odd_numbers(x):
    for i in x:
        if i % 2 == 1:
            yield i

def odd_numbers_highest(x):
    biggest_set =  deque(maxlen=10)
    for i in x:
        if i % 2 == 1:
            yield i, biggest_set
            biggest_set.append(i)

if __name__ == '__main__':
    test_group = [x for x in range(1, 101, 1)]
    print(test_group)
    # print(deque())
    #
    # for i in odd_numbers(test_group):
    #     print(i)

    for i, biggest in odd_numbers_highest(test_group):
        print(i)
        print(biggest)