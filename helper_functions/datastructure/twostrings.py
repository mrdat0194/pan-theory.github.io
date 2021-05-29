#!/bin/python3

import os


# Complete the twoStrings function below.
def twoStrings(s1, s2):
    '''

    :param s1:
    :param s2:
    :return:
    '''
    s1 = set(s1)
    s2 = set(s2)
    result = s1.intersection(s2)
    print(result)
    if not result:
        print('NO')
        return 'NO'
    else:
        print('YES')
        return 'YES'

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    output = os.path.join(BASE_DIR, "twoStrings.txt")
    if os.path.exists(output):
        f = open(output, "r+")
    else:
        f = open(output, "w")

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        f.write(result + '\n')

    f.close()
# 1
# hello
# world
