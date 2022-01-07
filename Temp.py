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

# https://github.com/vbartle/VMLS-Companions

# Daily Coding Problem: Problem #375
# [4, 1, 0, 2, 3]
# This means the researcher has 5 papers with 4, 1, 0, 2, and 3
# citations respectively. The h-index for this researcher is 2,
# since they have 2 papers with at least 2 citations and
# the remaining 3 papers have no more than 2 citations.

# def h_index(lst):
#     result = 0
#     for i, num_citations in enumerate(reversed(sorted(lst))):
#         if num_citations > i:
#             result = i + 1
#         else:
#             break
#     return result

# lst = [-1, 5, 13, 8, 2, 3, 3, 1]
# k = 5
# sliding_window_median(lst, k)
# from bisect import insort
#
# def sliding_window_median(lst, k):
#     window = sorted(lst[:k])
#     print(window)
#     for num_to_remove, num in zip(lst, lst[k:]+[0]):
#         print((window[int(k / 2)] + window[~int(k / 2)]) / 2.0)
#         window.remove(num_to_remove)
#         insort(window, num)
#         print(window)

# Daily Coding Problem: Problem #385
# This problem was asked by Apple.
#
# You are given a hexadecimal-encoded string that has been XOR'd against a single char.
#
# Decrypt the message. For example, given the string:
#
# 7a575e5e5d12455d405e561254405d5f1276535b5e4b12715d565b5c551262405d505e575f
#
# def xor_decipher(s):
#     '''
#         s = '7a575e5e5d12455d405e561254405d5f1276535b5e4b12715d565b5c551262405d505e575f'
#         xor_decipher(s)
#     '''
#     b = bytearray.fromhex(s)
#
#     for char in range(256):
#         result = []
#         for byte in b:
#             result.append(byte ^ char)
#
#         print(bytes(result).decode())

# Daily Coding Problem: Problem #390
# You are given an unsorted list of 999,000 unique integers, each from 1 and 1,000,000. Find the missing 1000 numbers.
# What is the computational and space complexity of your solution?
# def find_missing_nums(lst):
#     # Initialize our bitarray and set
#     bitarray = [False for _ in range(1000000)]
#     s = set(lst)
#
#     # Go over nums from 1 to n + 1
#     for i in range(1, 1000001):
#         if i in s:
#             bitarray[i - 1] = True
#
#     # Iterate over bitarray, generate results
#     results = []
#     for i in range(1, 1000001):
#         if not bitarray[i - 1]:
#             results.append(i)
#     return results


# Daily Coding Problem: Problem #391
# user1 = ['/home', '/register', '/login', '/user', '/one', '/two']
# user2 = ['/home', '/red', '/login', '/user', '/one', '/pink']
# You should return the following:
#
# ['/login', '/user', '/one']
# def longest_contiguous_history(user1, user2):
#     longest_result = []
#     for i in range(len(user1)):
#         for j in range(i + 1, len(user1) + 1):
#             subarray1 = user1[i:j]
#
#             for k in range(len(user2) - len(subarray1)):
#                 subarray2 = user2[k:k + len(subarray1)]
#                 if subarray1 == subarray2 and len(subarray1) > len(longest_result):
#                     longest_result = subarray1
#
#     return longest_result

# Daily Coding Problem: Problem #392
# Determine the perimeter of this island.
#
# For example, given the following matrix:
#
# [[0, 1, 1, 0],
#  [1, 1, 1, 0],
#  [0, 1, 1, 0],
#  [0, 0, 1, 0]]
# Return 14.
# def get_num_neighbours(board, r, c):
#     num = 0
#     if r > 0:
#         num += board[r - 1][c] == 1
#
#     if r < len(board) - 1:
#         num += board[r + 1][c] == 1
#
#     if c > 0:
#         num += board[r][c - 1] == 1
#
#     if c < len(board[0]) - 1:
#         num += board[r][c + 1] == 1
#
#     return num
#
#
# def island_perimeter(board):
#     perimeter = 0
#     for r, row in enumerate(board):
#         for c, val in enumerate(row):
#             if val == 1:
#                 perimeter += 4 - get_num_neighbours(board, r, c)
#     return perimeter

# Daily Coding Problem: Problem #395
# This problem was asked by Robinhood.
#
# Given an array of strings, group anagrams together.
#
# For example, given the following array:
#
# ['eat', 'ate', 'apt', 'pat', 'tea', 'now']
# Return:
#
# [['eat', 'ate', 'tea'],
#  ['apt', 'pat'],
#  ['now']]
#
# from collections import defaultdict
#
# def group_anagrams(words):
#     groups = defaultdict(list)
#     for word in words:
#         key = ''.join(sorted(word))
#         groups[key].append(word)
#
#     result = []
#     for group in groups.values():
#         result.append(group)
#     return result

# Daily Coding Problem: Problem #399
# Given a list of strictly positive integers, partition the list into 3 contiguous partitions which each sum up to the same value. If not possible, return null.
# # Python3 implementation of the given approach
# https://www.ijcai.org/Proceedings/09/Papers/096.pdf
# https://www.youtube.com/watch?v=ZaSMm2xvatw
# # This function returns true if the array
# # can be divided into three equal sum segments
# Function to check if all subsets are filled or not
# def checkSum(sumLeft, k):
#
#     r = True
#     for i in range(k):
#         if sumLeft[i]:
#             r = False
#
#     return r
# Helper function for solving `k` partition problem.
# It returns true if there exist `k` subsets with the given sum
# def subsetSum(S, n, sumLeft, A, k):
#
#     # return true if a subset is found
#     if checkSum(sumLeft, k):
#         return True
#
#     # base case: no items left
#     if n < 0:
#         return False
#
#     result = False
#
#     # consider current item `S[n]` and explore all possibilities
#     # using backtracking
#     for i in range(k):
#         if not result and (sumLeft[i] - S[n]) >= 0:
#
#             # mark the current element subset
#             A[n] = i + 1
#
#             # add the current item to the i'th subset
#             sumLeft[i] = sumLeft[i] - S[n]
#             print('sum1',sumLeft)
#
#             # recur for remaining items
#             result = subsetSum(S, n - 1, sumLeft, A, k)
#
#             # backtrack: remove the current item from the i'th subset
#             sumLeft[i] = sumLeft[i] + S[n]
#             print('sum2',sumLeft)
#
#     # return true if we get a solution
#     return result
#
#
# # Function for solving k–partition problem. It prints the subsets if
# # set `S[0…n-1]` can be divided into `k` subsets with equal sum
# def partition(S, k):
#
#     # get the total number of items in `S`
#     n = len(S)
#
#     # base case
#     if n < k:
#         print("k-partition of set S is not possible")
#         return
#
#     # get the sum of all elements in the set
#     total = sum(S)
#     A = [None] * n
#
#     # create a list of size `k` for each subset and initialize it
#     # by their expected sum, i.e., `sum/k`
#     sumLeft = [total // k] * k
#     # print(sumLeft)
#
#     # return true if the sum is divisible by `k` and set `S` can
#     # be divided into `k` subsets with equal sum
#     result = (total % k) == 0 and subsetSum(S, n - 1, sumLeft, A, k)
#
#     if not result:
#         print("k-partition of set S is not possible")
#         return
#
#     # print all k–partitions
#     for i in range(k):
#         print(f"Partition {i} is", [S[j] for j in range(n) if A[j] == i + 1])
#
#
# # Input: a set of integers
# S = [7, 3, 5, 12, 2, 1, 5, 3, 8, 4, 6, 4]
# k = 5
#
# partition(S, k)
#
# https://newsletterest.com/newsletters/2109/Daily%20Coding%20Problem?pageIndex=13
# Daily Coding Problem #405
# Given a tree, find the largest tree/subtree that is a BST.
#
# Given a tree, return the size of the largest tree/subtree that is a BST.

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def is_bst(root):
    def is_bst_helper(root, min_key, max_key):
        if root is None:
            return True
        if root.key <= min_key or root.key >= max_key:
            return False
        return is_bst_helper(root.left, min_key, root.key) and \
               is_bst_helper(root.right, root.key, max_key)

    return is_bst_helper(root, float('-inf'), float('inf'))

def size(root):
    if root is None:
        return 0
    return size(root.left) + size(root.right) + 1

def largest_bst_subtree(root):
    def helper(root):
        # Returns a tuple of (size, root) of the largest subtree.
        if is_bst(root):
            return (size(root), root)
        return max(helper(root.left), helper(root.right), key=lambda x: x[0])

    return helper(root)[1]

def largest_bst_subtree(root):
    max_size = 0
    max_root = None
    def helper(root):
        # Returns a tuple of (size, min_key, max_key) of the subtree.
        nonlocal max_size
        nonlocal max_root
        if root is None:
            return (0, float('inf'), float('-inf'))
        left = helper(root.left)
        right = helper(root.right)
        if root.key > left[2] and root.key < right[1]:
            size = left[0] + right[0] + 1
            if size > max_size:
                max_size = size
                max_root = root
            return (size, min(root.key, left[1]), max(root.key, right[2]))
        else:
            return (0, float('-inf'), float('inf'))

    helper(root)
    return max_root

self.tree = BST()
self.tree.insert(10)
self.tree.insert(15)
self.tree.insert(6)
self.tree.insert(4)
self.tree.insert(9)
self.tree.insert(12)
self.tree.insert(24)
self.tree.insert(7)
self.tree.insert(20)
self.tree.insert(30)
self.tree.insert(18)

if __name__ == '__main__':
    pass


