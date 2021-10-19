# https://oj.vnoi.info/user

import math
import numpy as np

# Ví dụ, tập hợp 𝐴=2,3,5,8,11,13 là tập hợp phản nhị phân, tập hợp 𝐵=2,3,5,6,8,11,13 không phải, do nó chứa 2 số 3 và 6.

def antiBinary(x, memo):
    if x == 1:
        return 0
    if x == 2:
        return 1
    if x not in memo:
        if x % 2 == 0:
            memo += 1
            antiBinary(x - 1, memo)
            return memo


    """
5
11
12
13
14
15
    n = input()
    for _ in range(int(n)):
        x = int(input())
        myDict = {}
        result = antiBinary(x,myDict)
        print(result)
        
    :return:
    """


######
class euler_totient:
    # https://cp-algorithms.com/algebra/phi-function.html#toc-tgt-6
    # def primeDec(a):
    #     n = a
    #     prime_list = {}
    #     x = 2
    #     while x * x <= a:
    #         while n % x == 0:
    #             n //= x
    #             prime_list[x] = 1
    #         x += 1
    #     if n != 1:
    #         prime_list[n] = 1
    #     return prime_list
    #
    # def euler(a):
    #     target = a
    #     primes = primeDec(a)
    #     for key in primes.keys():
    #         target -= target // key
    #     return target
    #
    # def find(a, m):
    #     """
    # 4
    # 2 4
    # 3 5
    # 9 6
    # 10 7
    #
    # 3
    # 177 168
    # 2028 88772
    # 123456789 987654321
    #
    #     :param a:
    #     :param m:
    #     :return:
    #     """
    #     if pow(a, m, m) == 0:
    #         return m
    #     if a == 1:
    #         return 1
    #     phim = euler(m)
    #     return pow(a, find(a, phim), lcm(m, phim))
    #
    # def lcm(m, phim):
    #     return (m * phim) // math.gcd(m, phim)
    #
    import math
    def prime_division(n):
        x = 2
        d = {}
        while x * x <= n:
            while n % x == 0:
                n //= x
                d[x] = d.get(x, 0) + 1
            x += 1
        if n > 1:
            d[n] = d.get(n, 0) + 1
        return d

    def phi(n):
        for p in euler_totient.prime_division(n):
            n = (n*(p-1))//p
        return n


    def lcm(x, y):
        return x*y // math.gcd(x, y)

    def solve(A, M):
        if pow(A, M, M) == 0:
            return M
        if 1 in {A, M}:
            return 1

        phiM = euler_totient.phi(M)

        return pow(A, euler_totient.solve(A, phiM), euler_totient.lcm(phiM, M))


    def main():
        """
    4
    3 8
    2 4
    9 6
    10 7

    3
    123456789 987654321
    177 168
    2028 88772

    euler_toitient.main()

        :return:
        """
        Q = int(input())
        for _ in range(Q):
            a, m = map(int, input().split())
            print(euler_totient.solve(a, m))


from bisect import bisect_left


def LongestIncreasingSubsequenceLength(v):
    """
        # Driver program to test above function
        v = [2, 5, 3, 7, 11, 8, 10, 13, 6]
        print("Length of Longest Increasing Subsequence is ",
        LongestIncreasingSubsequenceLength(v))
    :param v:
    :return:
    """
    if len(v) == 0:  # boundary case
        return 0

    tail = [0 for i in range(len(v) + 1)]
    length = 1  # always points empty slot in tail

    tail[0] = v[0]

    for i in range(1, len(v)):
        if v[i] > tail[length-1]:
            # v[i] extends the largest subsequence
            tail[length] = v[i]
            length += 1

        else:
            # v[i] will extend a subsequence and discard older subsequence

            # find the largest value just smaller than v[i] in tail

            # to find that value do binary search for the v[i] in
            # the range from begin to 0 + length

            # bisect function either returns index where element is found
            # or the appropriate index at which element should be placed

            # finally replace the existing subsequene with new end value
            print(tail)
            tail[bisect_left(tail, v[i], 0, length-1)] = v[i]
            print(tail)
            print(bisect_left(tail, v[i], 0, length-1))
    return length


def multiply(A,B):
    n = 1

    while (n < len(A)+ len(B)):
        n <<= 1

    A = np.array(A)
    A.resize(n)
    B = np.array(B)
    B.resize(n)


    Fa = np.fft.fft(A)
    Fb = np.fft.fft(B)

    FA = Fa*Fb

    FA = np.fft.ifft(FA)

    result = list()

    for i in range(n):
        result.append(round(FA[i].real))

    return result

def findCount(Arr1, Arr2):
    MAX = max(max(Arr1), max(Arr2))

    n = len(Arr1)
    m = len(Arr2)

    A = [0]*(MAX+1)
    for i in range(n):
        A[Arr1[i]] += 1

    B = [0]*(MAX+1)
    for i in range(m):
        B[Arr2[i]] += 1


    P = multiply(A,B)


    for i in range(2*MAX+1):
        if P[i] > 0:
            print(str(i) + "->" + str(P[i]))


if __name__=='__main__':
    arr1 = [1, 2]
    arr2 = [1, 2, 1]
    findCount(arr1, arr2)







