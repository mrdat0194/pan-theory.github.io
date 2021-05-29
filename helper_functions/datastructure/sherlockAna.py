#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#T = int(input().strip())
#for a0 in range(T):
#    s = input().strip()
#    anag = 0
#    map = {}
#    for i in range(len(s)):
#        for j in range(len(s) - i):
#            s1 = ''.join(sorted(s[j:j + i + 1]))
#            map[s1] = map.get(s1, 0) + 1
#    for key in map:
#        anag += (map[key] - 1) * map[key] // 2
#    print(anag)

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(string):
    '''
    # 2
    # ifailuhkqq
    # kkkk
    For the first query, we have anagram pairs  and  at positions  and  respectively.

    For the second query:
    There are 6 anagrams of the form  at positions  and .
    There are 3 anagrams of the form  at positions  and .
    There is 1 anagram of the form  at position .
    :param string:
    :return:
    '''
    buckets = {}
    for i in range(len(string)):
        for j in range(1, len(string) - i + 1):
            key = frozenset(Counter(string[i:i+j]).items()) # O(N) time key extract
            # print(key)
            buckets[key] = buckets.get(key, 0) + 1
    count = 0
    # print(buckets)
    for key in buckets:
        count += buckets[key] * (buckets[key]-1) // 2
    return count

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    output = os.path.join(BASE_DIR, "SherlockAna.txt")
    if os.path.exists(output):
        f = open(output, "r+")
    else:
        f = open(output, "w")

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        f.write(str(result) + '\n')

    f.close()

