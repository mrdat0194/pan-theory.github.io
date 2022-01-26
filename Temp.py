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

# nelder-mead for multimodal function optimization
from scipy.optimize import minimize
from numpy.random import rand
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi


# # objective function
# def objective(v):
#     x, y = v
#     return -20.0 * exp(-0.2 * sqrt(0.5 * (x ** 2 + y ** 2))) - exp(0.5 * (cos(2 * pi * x) + cos(2 * pi * y))) + e + 20
#
# # define range for input
# r_min, r_max = -5.0, 5.0
# # define the starting point as a random sample from the domain
# pt = r_min + rand(2) * (r_max - r_min)
# # perform the search
# result = minimize(objective, pt, method='nelder-mead')
# # summarize the result
# print('Status : %s' % result['message'])
# print('Total Evaluations: %d' % result['nfev'])
# # evaluate solution
# solution = result['x']
# evaluation = objective(solution)
# print('Solution: f(%s) = %.5f' % (solution, evaluation))

if __name__ == '__main__':
    from sys import stdin

    mod = 998244353


    def power(n, k):
        if k == 0:
            return 1
        x = 1
        while k > 1:
            if k % 2 == 0:
                n = n * n % mod
            else:
                x = n * x % mod
                n = n * n % mod
            k //= 2
        return n * x % mod


    def get_pow2(k):
        pow2 = 1
        logpow2 = 0
        while pow2 <= k:
            pow2 *= 2
            logpow2 += 1
        invpow2 = power(pow2, mod - 2)
        return pow2, logpow2, invpow2


    def NTT(p, r, pow2, logpow2, invpow2, forward):
        j = pow2 // 2
        for i in range(1, pow2 - 1):
            if i >= j:
                p[i], p[j] = p[j], p[i]
            k = pow2 // 2
            while True:
                if k > j:
                    break
                j -= k
                k //= 2
            j += k
        l = 2
        m = len(r) * forward
        for _ in range(logpow2):
            for j in range(l // 2):
                for k in range(j, pow2, l):
                    a = p[k]
                    b = r[j * m // l] * p[k + l // 2]
                    b %= mod
                    p[k] = (a + b) % mod
                    p[k + l // 2] = (a - b) % mod
            l *= 2
        if forward == -1:
            for i in range(pow2):
                p[i] *= invpow2
                p[i] %= mod


    def get_answer(c, v, n, s, k):
        pow2, logpow2, invpow2 = get_pow2(2 * k)
        prim_root = power(3, (mod - 1) // pow2)
        r = [1] * pow2
        for i in range(1, pow2):
            r[i] = r[i - 1] * prim_root
            r[i] %= mod
        factorial = [1] * pow2
        factorial_inv = [1] * pow2
        for i in range(1, pow2):
            factorial[i] = factorial[i - 1] * i
            factorial[i] %= mod
            factorial_inv[i] = power(factorial[i], mod - 2)
        vpowers = [[1] * pow2 for _ in range(n + 1)]
        for i in range(1, n + 1):
            for l in range(1, pow2):
                vpowers[i][l] = vpowers[i][l - 1] * v[i]
                vpowers[i][l] %= mod
        dp = [[0] * (k + 1) for _ in range(s + 1)]
        dp[0][0] = 1
        p1 = [0] * pow2
        p2 = [0] * pow2
        for i in range(1, n + 1):
            for j in range(s, c[i] - 1, -1):
                for l in range(pow2):
                    if l <= k:
                        p1[l] = dp[j - c[i]][l] * factorial_inv[l] % mod
                        p2[l] = factorial_inv[l] * vpowers[i][l] % mod
                    else:
                        p1[l] = 0
                        p2[l] = 0
                NTT(p1, r, pow2, logpow2, invpow2, 1)
                NTT(p2, r, pow2, logpow2, invpow2, 1)
                for l in range(pow2):
                    p1[l] *= p2[l]
                    p1[l] %= mod
                NTT(p1, r, pow2, logpow2, invpow2, -1)
                for l in range(k + 1):
                    dp[j][l] += p1[l] * factorial[l]
                    dp[j][l] %= mod
        answer = 0
        for j in range(s + 1):
            answer += dp[j][k]
            answer %= mod
        print(answer)


    def solve():
        n, s, k = list(map(int, stdin.readline().strip().split()))
        c = [0] * (n + 1)
        v = [0] * (n + 1)
        for i in range(n):
            c[i + 1], v[i + 1] = list(map(int, stdin.readline().strip().split()))
        get_answer(c, v, n, s, k)
        stdin.close()


    solve()

# 3 2 2
# 1 2
# 2 3
# 1 4


# from typing import List
# from collections import defaultdict
#
#
# class Solution:
#     def findJudge(self, N: int, trust: List[List[int]]) -> int:
#         """
#         like the find the celebrity
#         """
#         ingress = defaultdict(set)
#         egress =defaultdict(set)
#         for p, q in trust:
#             egress[p].add(q)
#             ingress[q].add(p)
#         for i in range(1, N+1):
#             if len(egress[i]) == 0 and len(ingress[i]) == N - 1:
#                 return i
#         return -1
# 2 , [1,2]

