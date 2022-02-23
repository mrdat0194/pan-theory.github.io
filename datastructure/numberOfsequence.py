#!/bin/python3
# https://www.hackerrank.com/contests/w22/challenges/number-of-sequences/
import itertools
from math import factorial


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2::i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return [2] + [2 * i + 1 for i in range(1, n // 2) if sieve[i]]


def number_nice(A):
    if A[0] != 0 and A[0] != -1:
        return 0
    # elif len(A)==2
    else:
        nice_seqs = 1
        N = len(A)
        # a[1] = 0 always
        # a[2] = 0 or 1
        for prime in primes(N + 1):
            # print(prime)
            positions = [i for i in range(N) if
                         (i + 1) % prime == 0]  # all positions at multiples of prime in A, 0-indexed
            test = [A[i] for i in positions]
            # print(test)
            fixed_mods = [x % prime for x in test if x != -1]

            if len(set(fixed_mods)) > 1:
                return 0  # given sequence contains contradiction, cannot be fixed

            elif -1 not in test:
                continue  # if nothing changeable and every element in sequence mod prime is equal, move to next prime

            elif -1 in test and len(set(test)) == 1:  # all -1's
                nice_seqs *= prime * factorial((positions[-1] + 1) / prime)

            else:  # mixture of -1's and elements with equal mods wrt prime
                the_remainder = fixed_mods[0]
                minus_ones = [i + 1 for i in positions if A[i] == -1]  # 1-indexed positions of -1's in test
                for position in minus_ones:
                    nice_seqs *= position / prime
    return nice_seqs


n = int(input().strip())
arr = [int(x) for x in input().strip().split(' ')]

print(number_nice(arr) % (7 + 10 ** 9))