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

if __name__ == '__main__':
    pass

