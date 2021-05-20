import os
import math
import random
import re
import sys
from collections import Counter
from functools import cmp_to_key

class story_teller:
    def sockMerchant(n, ar):
        '''

        :param n:how many socks : 9
        :param ar: 10 20 20 10 10 30 50 10 20
        :return: sum of pair of sock
        '''
        sum=0
        for values in Counter(ar).values():
            sum+=values//2
        return sum

    def countingValleys(n, s):
        '''

        :param :n 8
        :param s: UDDDUDUU
        :return: up and down how many valley
        '''
        UD = {'U': 1, 'D': -1}
        sea_level = 0
        valley = 0
        for step in s:
            sea_level = sea_level + UD[step]
            if not sea_level and step == 'U':
                valley += 1
        return valley

    def repeatedString(s, n):
        '''

        :param s: aba
        :param n: 10 of letters contain abaabaabaa
        :return: how many a
        '''
        return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")

    def countTriplets(arr, r):
        '''
        Counting how many triplet of the group of exponential
        # 5 5
        # 1 5 5 25 125
        :param arr: increasing seq
        :param r: num of exp
        :return:
        '''
        a = Counter(arr)
        b = Counter()
        s = 0
        for i in arr:
            # số chia
            j = i//r
            # số nhân
            k = i*r
            a[i]-=1
            # số lưu tạo đc bao nhiêu cặp 3
            if b[j] and a[k] and not i%r:
                s+=b[j]*a[k]
            b[i]+=1
        return s

class Player:
    '''
    5
    amy 100
    david 100
    heraldo 50
    aakansha 75
    aleksa 150
    '''
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        pass
    def comparator(a, b):
        val = b.score - a.score
        if val == 0:
            return -1 if a.name < b.name else 1
        print(val)
        return val

    def compareTriplets(a, b):
        '''
        :param a: list point a 17 28 30
        :param b: list point b 99 16 8
        :return:
        '''
        A = a
        B = b
        C = sum([1 if x[0] > x[1] else 0 for x in zip(A,B)])
        D = sum([1 if x[1] > x[0] else 0 for x in zip(A,B)])
        return [C, D]

class Solution(object):
    def nextPermutation(self, nums):
        """
        https://www.nayuki.io/res/next-lexicographical-permutation-algorithm/nextperm.py
        :type nums: List[int]
        :rtype: list and arr modified to the next smallest permutation
        """
        arr = nums
        # Find non-increasing suffix
        i = len(arr) - 1
        while i > 0 and arr[i - 1] >= arr[i]:
            i -= 1
        if i <= 0:
            return False

        # Find successor to pivot
        j = len(arr) - 1
        while arr[j] <= arr[i - 1]:
            j -= 1
        arr[i - 1], arr[j] = arr[j], arr[i - 1]

        # Reverse suffix
        arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
        print(arr)
        return True

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    # #Socks

    # output = os.path.join(BASE_DIR, "output_sock.txt")
    # if os.path.exists(output):
    #     f = open(output, "r+")
    # else:
    #     f = open(output, "w")

    # n = int(input())
    # ar = list(map(int, input().rstrip().split()))
    # result = story_teller.sockMerchant(n, ar)

    # f.write(str(result))
    # f.close()
    # myfile = open(output, 'r+')
    # print(myfile.readlines())

    # # countingValleys

    # output = os.path.join(BASE_DIR, "valleycount.txt")
    # if os.path.exists(output):
    #     f = open(output, "r+")
    # else:
    #     f = open(output, "w")
    #
    # n = int(input())
    # s = input()
    # result = story_teller.countingValleys(n, s)
    #
    # f.write(str(result))
    # f.close()
    # myfile = open(output, 'r+')
    # print(myfile.readlines())

    # # repeatedstrings

    # output = os.path.join(BASE_DIR, "repeatedstrings.txt")
    # if os.path.exists(output):
    #     f = open(output, "r+")
    # else:
    #     f = open(output, "w")
    #
    # s = input()
    # n = int(input())
    # result = story_teller.repeatedString(s, n)
    #
    # f.write(str(result))
    # f.close()
    # myfile = open(output, 'r+')
    # print(myfile.readlines())

    # # compare_award

    # output = os.path.join(BASE_DIR, "compareTriplets.txt")
    # if os.path.exists(output):
    #     f = open(output, "r+")
    # else:
    #     f = open(output, "w")
    #
    # a = list(map(int, input().rstrip().split()))
    # b = list(map(int, input().rstrip().split()))
    # result = Player.compareTriplets(a, b)
    # f.write(' '.join(map(str, result)))
    # f.write('\n')
    # f.close()
    # myfile = open(output, 'r+')
    # print(myfile.readlines())

    # # Name - Score compare one another
    # n = int(input())
    # data = []
    # for i in range(n):
    #     name, score = input().split()
    #     score = int(score)
    #     player = Player(name, score)
    #     data.append(player)
    # data = sorted(data, key=cmp_to_key(Player.comparator))
    # for i in data:
    #     print(i.name, i.score)

    # # Counttriplet how many triple that increase
    # n,r = map(int,input().split())
    # arr = list(map(int,input().split()))
    # print(countTriplets(arr, r))
