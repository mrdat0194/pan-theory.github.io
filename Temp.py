#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:16:49 2019

@author: petern
"""

# from my_functions import timer

# 1. move_file

# from my_functions import Complete_Function
#
# Complete_Function.Move_file.Data_move("hello.py" ,"/Users/petern/Desktop/samV/Project/", "/Users/petern/Desktop/samV/Project/helper_functions/")

# 1. append to excel
# Complete_Function.append_df_to_excel("/Users/petern/Desktop/hello.xlsx" ,"a")
# Given a list of integers and a number K, return which contiguous elements of the list sum to K.
#
# For example, if the list is [1, 2, 3, 4, 5] and K is 9, then it should return [2, 3, 4], since 2 + 3 + 4 = 9.


def constrained_compositions(n, m):
    # inputs: n is of type 'int' and m is a list of integers
    # output: a set of tuples

    k = len(m)
    parts = set()
    if k == n:
        if 1 <= min(m):
            parts.add((1,)*n)
    if k == 1:
        if n <= m[0]:
            parts.add((n,))
    else:
        for x in range(1, min(n-k+2,m[0]+1)):
            for y in constrained_compositions(n-x, m[1:]):
                parts.add((x,)+y)
    print(parts)
    return parts

# modify this cell

def face_sum(m, s):
    # inputs: m is list of integers and s is an integer
    # output: a variable of type 'float'
    # Example: Here we want to see to get the probability of largest face summing up to the number provided
    # As for [2,2], we have (1,1),(1,2),(2,1),(2,2) as all possible combinations of largest faces
    # For getting 3 as sum, we have its probability as 2/4 = 0.5
    l1= len(constrained_compositions(s,m))
    l2=1
    for i in m:
        l2= i*l2
    probability= l1/l2
    return probability

def compositions(k, n):
    # inputs: k and n are of type 'int'
    # output: a set of tuples
    if k == 1:
        return {(n,)}
    else:
        s = set()
        for i in range(1, n):
            for j in compositions(k - 1, n - i): #i + n-i = n
                s.add((i,) + j)
        return s

def constrained_sum_compositions(n, m):
    # inputs: n is of type 'int' and m is a list of integers
    # output: a set of tuples
    k = len(m)
    s = set()
    for c in compositions(k, n):
        print(c)
        if sum([c[i] <= m[i] for i in range(k)]) == k: #taking the sets of all comb. which are less than equal to the given
            s.add(c)
    return s

def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist


# functions = make_functions()
# for f in functions:
#     f()


def get_longest_uqsub(arr, seen=set()):
    '''
    Problem 189
    :param arr:
    :param seen:
    :return:
    '''
    if not arr:
        return len(seen)

    curr = arr[0]
    if curr in seen:
        return len(seen)

    seen_cp = seen.copy()
    seen_cp.add(curr)

    return max(get_longest_uqsub(arr[1:], seen_cp),
               get_longest_uqsub(arr[1:]))

# Tests
# assert get_longest_uqsub([]) == 0
# assert get_longest_uqsub([5, 5, 5]) == 1
# assert get_longest_uqsub([5, 1, 3, 5, 2, 3, 4, 1]) == 5
# assert get_longest_uqsub([5, 1, 3, 5, 2, 3, 4]) == 4
# assert get_longest_uqsub([5, 1, 3, 5, 2, 3]) == 4

if __name__ == '__main__':
    constrained_sum_compositions(9, [1, 2, 3, 4, 5])
    # get_longest_uqsub([5, 1, 3, 5, 2, 3, 4])


