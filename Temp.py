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
import torch.distributions as D

import os
from collections import OrderedDict


def compress_array(arr):
    compressed = []
    count = 1
    char = arr[0]
    for i in range(1,len(arr)):
      if arr[i] == char:
        count = count + 1
      else :
        compressed.append(char)
        compressed.append(count)
        char = arr[i]
        count = 1
    compressed.append(char)
    compressed.append(count)
    return compressed
#
# def compress_array(arr):
#     # Enter your code here
#     dict = OrderedDict.fromkeys(arr, 0)
#     print(dict)
#     for ch in arr:
#
#         dict[ch] += 1
#
#     output = []
#     for key, value in dict.items():
#         print(key)
#         print(value)
#         output.append(key)
#         output.append(str(value))
#     return output


# if __name__ == '__main__':
#
#     arr = [int(a) for a in input().split()]
#     result = compress_array(arr)
#     print(' '.join(map(str, result)))




