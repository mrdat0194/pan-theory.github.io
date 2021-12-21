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

if __name__ == '__main__':
    pass


