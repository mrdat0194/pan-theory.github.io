#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
from collections import Counter
def makeAnagram(a, b):
    '''
    How many deletion to make two string anagram
    :param a:
    :param b:
    :return:
    '''
    ct_a = Counter(a)
    ct_b = Counter(b)
    ct_a.subtract(ct_b)
    print(ct_a)
    print(ct_b)
    return sum(abs(i) for i in ct_a.values())
# cde
# abc

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    output = os.path.join(BASE_DIR, "output_makeAna.txt")

    if os.path.exists(output):
        f = open(output, "r+")
    else:
        f = open(output, "w")

    a = input()

    b = input()

    res = makeAnagram(a, b)

    f.write(str(res) + '\n')

    f.close()

