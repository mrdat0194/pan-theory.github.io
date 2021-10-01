#!/bin/python3

import os
import math
import random
import re
import sys
import itertools
from collections import Counter
from functools import cmp_to_key
from functools import partial
from collections import defaultdict

from my_functions.timer import print_param, timer

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class story_teller:
    @print_param("output_miniswap.txt", BASE_DIR)
    def minimumSwaps(arr):
        """
        Note: Minimum swap cannot solve wholy as minimumBribe
        swap to get a increasing order
        Given array
        After swapping  we get 1 3 4 2
        After swapping  we get 1 4 3 2
        After swapping  we get 1 2 3 4
        So, we need a minimum of 3 swaps to sort the array in ascending order

        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        res = minimumSwaps(arr)

        # 4
        # 4 3 1 2

        :param arr:
        :return:
        """
        ref_arr = sorted(arr)
        index_dict = {v: i for i,v in enumerate(arr)}
        swaps = 0

        for i,v in enumerate(arr):
            correct_value = ref_arr[i]
            if v != correct_value:
                to_swap_ix = index_dict[correct_value]
                arr[to_swap_ix],arr[i] = arr[i], arr[to_swap_ix]
                index_dict[v] = to_swap_ix
                index_dict[correct_value] = i
                swaps += 1
        return swaps

    def minimumBribes(Q):
        '''
        list of people in the queue, sequentially bribe the one in front of them
            [1,2,3,4,5] -> [4,1,2,3,5] -> [5,4,1,2,3] 7 steps -> [5,4,3,1,2] 9 steps
            Thought:

                Easy:
                [5,1,2,3,4]
                -> init: [4,0,1,2,3] -> enum: [0,1,2,3,4]

                Hard:
                [5,4,3,1,2]
                init:
                [4,3,2,0,1]
                enum:
                [0,1,2,3,4]

            at least how many bribes happened.

            t = int(input())

            for t_itr in range(t):
                n = int(input())

                q = list(map(int, input().rstrip().split()))

            story_teller.minimumBribes(q)
        # 2
        # 5
        # 2 1 5 3 4
        # 5
        # 2 5 1 3 4

        :param Q:
        :return:
        '''
        #
        # initialize the number of moves
        moves = 0
        #
        # decrease Q by 1 to make index-matching more intuitive
        # so that our values go from 0 to N-1, just like our
        # indices.  (Not necessary but makes it easier to
        # understand.)
        # Init:
        Q = [P-1 for P in Q]
        #
        # Loop through each person (P) in the queue (Q)
        for i,P in enumerate(Q):
            # i is the current position of P, while P is the
            # original position of P.
            #
            # First check if any P is more than two ahead of
            # its original position
            # if P - i > 5:
            #     print("Too chaotic")
            #     return
            #

            # From here on out, we don't care if P has moved
            # forwards, it is better to count how many times
            # P has RECEIVED a bribe, by looking at who is
            # ahead of P.  P's original position is the value
            # of P.
            # Anyone who bribed P cannot get to higher than
            # one position in front if P's original position,
            # so we need to look from one position in front
            # of P's original position to one in front of P's
            # current position, and see how many of those
            # positions in Q contain a number large than P.
            # In other words we will look from P-1 to i-1,
            # which in Python is range(P-1,i-1+1), or simply
            # range(P-1,i).  To make sure we don't try an
            # index less than zero, replace P-1 with
            # max P-1,0)

            for j in range(max(P-100,0),i):
                if Q[j] > P:
                    moves += 1
            print(moves)
            return moves

    @print_param("twoString.txt", BASE_DIR)
    def twoStrings(s1, s2):
        '''
            String that intersect
            # 1
            # hello
            # world
        :param s1:
        :param s2:
        :return:
        '''
        s1 = set(s1)
        s2 = set(s2)
        result = s1.intersection(s2)
        if not result:
            print('NO')
            return 'NO'
        else:
            print('YES')
            return 'YES'

    @print_param("SherlockAna.txt", BASE_DIR)
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

    @print_param("output_makeAna.txt", BASE_DIR)
    def makeAnagram(a, b):
        """
             How many deletion to make two string anagram

             a = input()
             b = input()
             story_teller.makeAnagram(a,b)

        :param a,b:
             cde
             abc
        :return:
        """

        ct_a = Counter(a)
        ct_b = Counter(b)
        ct_a.subtract(ct_b)
        return sum(abs(i) for i in ct_a.values())

    def checkMagazine(magazine, note):
        '''
        6 4
        give me one grand today night
        give one grand today
        completely contain in magazine as in note

            mn = input().split()

            m = int(mn[0])

            n = int(mn[1])

            magazine = input().rstrip().split()

            note = input().rstrip().split()

            print(ransom_note(magazine, note))
            print(checkMagazine(magazine, note))

        :param magazine:
        :param note:
        :return:
        '''
        d = {}
        for word in magazine:
            d.setdefault(word, 0)
            d[word] += 1
            # print(d)
        for word in note:
            if word in d:
                d[word] -= 1
            else:
                return False

        return all([x >= 0 for x in d.values()])


    def ransom_note(magazine, rasom):
        return (Counter(rasom) - Counter(magazine)) == {}

    @timer
    @print_param("output_sock.txt", BASE_DIR)
    def sockMerchant(n, ar):
        """
            sum of pair of sock
            n = int(input())
            ar = list(map(int, input().rstrip().split()))

        :param n:how many socks : 9
        :param ar: 10 20 20 10 10 30 50 10 20
        :return: sum of pair of sock
        """

        sum=0
        for values in Counter(ar).values():
            sum+=values//2
        return sum



    @print_param("output_freqQuery.txt", BASE_DIR)
    def freqQuery(queries):
        """
            command:
            1 - x : Insert x in your data structure.
            2 - y : Delete one occurence of y from your data structure, if present.
            3 - z : Check if any integer is present whose frequency is exactly . If yes, print 1 else 0

            q = int(input().strip())
            queries = []
            for _ in range(q):
                queries.append(list(map(int, input().rstrip().split())))

            story_teller.freqQuery(queries

        :param queries:
        8
        1 5
        1 6
        3 2
        1 10
        1 10
        1 6
        2 5
        3 2
        :return:[]
        """

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
        print(freqs)
        return results

    def coinChange(totalNumber, coins):
        """
            Greedy
            story_teller.coinChange(201, [1,2,5,20,50,100])

        :param coins: [1,2,5,20,50,100]
        :return:
        """
        N = totalNumber
        coins.sort()
        index = len(coins)-1
        while True:
            coinValue = coins[index]
            if N >= coinValue:
                print(coinValue)
                N = N - coinValue
            if N < coinValue:
                index -= 1

            if N == 0:
                break

    @print_param("valleycount.txt", BASE_DIR)
    def countingValleys(n, s):
        """
            countingValleys
            n = int(input())
            s = input()
            story_teller.countingValleys(n, s)

        :param :n 8
        :param s: UDDDUDUU
        :return: up and down how many valley
        """
        UD = {'U': 1, 'D': -1}
        sea_level = 0
        valley = 0
        for step in s:
            sea_level = sea_level + UD[step]
            if not sea_level and step == 'U':
                valley += 1
        return valley

    def construct_pyramid(lenMax):
        if lenMax % 2 == 1:
            peak = lenMax//2 + 1
            x_left = [x for x in range(1,peak)]
            x_right = list(reversed(x_left))
            pyramid = x_left + [peak] + x_right
            return pyramid

    def pyramid_build(n, ar):
        """
         You have N stones in a row, and would like to create from them a pyramid.
         This pyramid should be constructed such that the height of each stone increases by one until reaching the tallest stone,
         after which the heights decrease by one. In addition, the start and end stones of the pyramid should each be one stone high.
         You can change the height of any stone by paying a cost of 1 unit to lower its height by 1, as many times as necessary.
         Given this information, determine the lowest cost method to produce this pyramid.
         For example, given the stones [1, 1, 3, 3, 2, 1], the optimal solution is to pay 2 to create [0, 1, 2, 3, 2, 1]
            n = int(input())
            ar = list(map(int, input().rstrip().split()))
            story_teller.pyramid_build(n, ar)
        :param n: 6
        :param ar: 1 1 3 3 2 1
        1 1 1 5 1
        :return: [0, 1, 2, 3, 2, 1]

        """
        lenStone = n
        stones = ar
        lenMax = lenStone if lenStone % 2 else lenStone - 1
        cost = 0
        while lenMax > 0:
            pyramid = story_teller.construct_pyramid(lenMax)

            for offset in (0, lenStone - lenMax):
                valid = True
                for enum_index, enum_val in enumerate(pyramid):
                    stone_index = enum_index + offset
                    if enum_val > stones[stone_index]:
                        valid = False
                        break

                if valid:
                    result = [0]*offset + pyramid +[0]*(lenStone-offset-lenMax)
                    cost = sum([x[0] - x[1] for x in zip(stones,result)])
                    print(cost)
                    return result

            lenMax -= 2
        return []


    @print_param("repeatedstrings.txt", BASE_DIR)
    def repeatedString(s, n):
        """
            repeatedstrings
            s = input()
            n = int(input())
            result = story_teller.repeatedString(s, n)

        :param s: aba
        :param n: 10 of letters contain aba aba aba / a (phần dư)
        :return: how many a
        """
        return s.count("a") * (n // len(s)) + s[:n % len(s)].count("a")

    def countTriplets(arr, r):
        """
            Counting how many triplet of the group of exponential
            5 5
            1 5 5 25 125
            n,r = map(int,input().split())
            arr = list(map(int,input().split()))
            print(countTriplets(arr, r))

        :param arr: increasing seq
        :param r: num of exp
        :return: Counttriplet how many triple that increase


        """
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

    def formingMagicSquare(s):
        """
        convert it into a magic square at minimal cost. Print this cost on a new line.

        Note: The resulting magic square must contain distinct integers in the inclusive range [1-9]
            s = []
            for s_i in range(3):
                s += [int(s_temp) for s_temp in input().strip().split(' ')]
            result = formingMagicSquare(s)

        4 9 2
        3 5 7
        8 1 5
        :param s:
        :return:
        """
        squares = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6],
                   [0, 3, 6], [1, 4, 7], [2, 5, 8]]
        def ismagic(xs):
            for sq in squares:
                if sum(xs[s] for s in sq) != 15:
                    return False
            return True

        gen = filter(ismagic, list(itertools.permutations(range(1,10))))

        return min(sum(abs(x - y) for x, y in zip(gl, s)) for gl in gen)

class problem308:
    """
    # Determine the number of ways to group the array elements using parentheses so that the entire expression evaluates to True.
    #
    # For example, suppose the input is ['F', '|', 'T', '&', 'T']. In this case, there are two acceptable groupings: (F | T) & T and F | (T & T).
    """
    def split(expression):
        operands, operators = [], []

        for value in expression:
            if value in {'T', 'F'}:
                operands.append(value)
            else:
                operators.append(value)

        return operands, operators

    def solve(expression):
        operands, operators = problem308.split(expression)

        n = len(operands)
        T = [[0 for _ in range(n)] for _ in range(n)]
        F = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            if operands[i] == 'T':
                T[i][i] = 1; F[i][i] = 0
            else:
                T[i][i] = 0; F[i][i] = 1

        for gap in range(1, n):
            for i in range(n - gap):
                j = i + gap

                for k in range(i, j):
                    all_options = (T[i][k] + F[i][k]) * (T[k+1][j] + F[k+1][j])

                    if operators[k] == '&':
                        T[i][j] += T[i][k] * T[k+1][j]
                        F[i][j] += (all_options - T[i][j])

                    elif operators[k] == '|':
                        F[i][j] += F[i][k] * F[k+1][j]
                        T[i][j] += (all_options - F[i][j])

                    elif operators[k] == '^':
                        T[i][j] += F[i][k] * T[k+1][j] + T[i][k] * F[k+1][j]
                        F[i][j] += T[i][k] * T[k+1][j] + F[i][k] * F[k+1][j]

        return T[0][n - 1]

class Player:
    """
        series play
    """
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        pass
    def comparator(a, b):
        val = b.score - a.score
        if val == 0:
            return -1 if a.name < b.name else 1
        return val
    def score_billboard(data):
        """
        Name - Score compare one another
        n = int(input())
        data = []
        for i in range(n):
            name, score = input().split()
            score = int(score)
            player = Player(name, score)
            data.append(player)
        Player.score_billboard(data)

        data append Player
        5
        amy 100
        david 100
        heraldo 50
        aakansha 75
        aleksa 150
        :return:
        """
        data = sorted(data, key=cmp_to_key(Player.comparator))
        for i in data:
            print(i.name, i.score)


    @print_param("compareTriplets.txt", BASE_DIR)
    def compareTriplets(a, b):
        """
            compare_award
            a = list(map(int, input().rstrip().split()))
            b = list(map(int, input().rstrip().split()))

        :param a: list point a 17 28 30
        :param b: list point b 99 16 8
        :return: point for each player in each round
        """
        A = a
        B = b
        C = sum([1 if x[0] > x[1] else 0 for x in zip(A,B)])
        D = sum([1 if x[1] > x[0] else 0 for x in zip(A,B)])
        return [C, D]

class Solution(object):
    def nextPermutation(self, nums):
        """
            #   arr = [0, 1, 0]
            #   next_permutation(arr)  (returns True)
            #   arr has been modified to be [1, 0, 0]
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
        print(arr)
        arr[i:] = arr[len(arr) - 1 : i - 1 : -1]
        print(arr)
        return True

class MySpecialQueue:
    """
    Special queue to get the highest bidder to maximize profit
    """
    def __init__(self):
        # Do not change the variable name of self.queue
        self.queue = None

    def insert(self, data):

        if self.queue == None:
            self.queue = [data]
        else:
            if data != '':
                self.queue.append(data)


    def dequeue(self):
        largest = max(self.queue)
        self.queue.remove(largest)

    def leftover_bidders( bids, number_of_items ) :
        """
        print(MySpecialQueue.leftover_bidders([1,2,3,4,5,6,7,8,9,], 2 ))

        :param bids:
        :param number_of_items:
        :return:
        """
        ######### DO NOT MODIFY BELOW ###########
        myQueue = MySpecialQueue()

        for bid in bids:
            myQueue.insert(bid)
        for sale in range(number_of_items):
            myQueue.dequeue()

        return myQueue.queue if myQueue.queue else [None]

        ######### DO NOT MODIFY ABOVE ###########

class Stock:
    pass

if __name__ == '__main__':

    print(MySpecialQueue.leftover_bidders([1,2,3,4,5,6,7,8,9,], 2 ))



