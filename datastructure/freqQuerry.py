#!/bin/python3

import os
from collections import defaultdict

# Complete the freqQuery function below.
def freqQuery(queries):
    '''
    command:
    1 - x : Insert x in your data structure.
    2 - y : Delete one occurence of y from your data structure, if present.
    3 - z : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0
    :param queries: 
    :return:
    '''
    results = []
    lookup = dict()
    freqs = defaultdict(set)
    for command, value in queries:
        freq = lookup.get(value, 0)
        if command == 1:
            lookup[value] = freq + 1
            freqs[freq].discard(value)
            freqs[freq + 1].add(value)
        elif command == 2:
            lookup[value] = max(0, freq - 1)
            freqs[freq].discard(value)
            freqs[freq - 1].add(value)
        elif command == 3:
            results.append(1 if freqs[value] else 0)
    return results

# 8
# 1 5
# 1 6
# 3 2
# 1 10
# 1 10
# 1 6
# 2 5
# 3 2

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    output = os.path.join(BASE_DIR, "output_freqQuery.txt")
    if os.path.exists(output):
        f = open(output, "r+")
    else:
        f = open(output, "w")

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    f.write('\n'.join(map(str, ans)))
    f.write('\n')
    f.close()
    myfile = open(output, 'r+')
    print(myfile.readlines())

