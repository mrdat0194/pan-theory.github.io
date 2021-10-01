# -*- coding: utf-8 -*-
"""
Pycharm Editor

This is a temporary finished file.
"""
import math
import os
import random
import re
import sys
import itertools
from collections import Counter
from functools import reduce
from bisect import bisect_right, bisect_left
from heapq import heapify, heappop, heappush
import numpy as np

from functools import reduce #python 3
#
# product = reduce((lambda x, y: x * y), [1, 2, 3, 4])


# # 0
# n, d = (3,5)
# arr = (1,2,3,4,5)
# print(type(arr))
# d %= n
# print(d)
# print(*(arr[d:] + arr[:d]))

# # 1
# my_dict = {
#     "out" :"Dat",
#     "in" : "Dat",
#     "on" : "Hanh",
#     "out" : "Hanh"
# }
# my_list = list(set(my_dict.values()))
# print(my_dict.values())
# print(set(my_dict.values()))
# print(my_dict.items())
# new_dict = {}
# for k in my_list:
#     for key,value in my_dict.items():
#         if k in value:
#             if new_dict == {}:
#                 new_dict = {value: [key]}
#             else:
#                 if k in new_dict.keys():
#                     new_dict[value].append(key)
#                     # print(new_dict)
#                 else:
#                     new_dict[k] = [key]
#
# print(new_dict)

# # 2
# c = dict(zip(['A', 'Z'], [1, -1]))
# d = dict([('A', 1), ('Z', -1)])
# e = dict({'Z': -1, 'A': 1})
# list(zip(['h', 'e', 'l', 'l', 'o'], [1, 2, 3, 4, 5]))
# list(zip('hello', range(1, 6)))

# ##
# def diagonalDifference(a):
#     # Complete this function
#     sum1  = 0
#     sum2  = 0
#     for i in range(n):
#         sum1 += int(a[i][i])
#         sum2 += int(a[i][n-i-1])
#     return abs(sum1 - sum2)
# #
# # if __name__ == '__main__':
# #     fptr = open(os.environ['OUTPUT_PATH'], 'w')
# #
# #     n = int(input().strip())
# #
# #     arr = []
# #
# #     for _ in range(n):
# #         arr.append(list(map(int, input().rstrip().split())))
# #
# #     result = diagonalDifference(arr)
# #
# #     fptr.write(str(result) + '\n')
# #
# #     fptr.close()
#
# ##
#

#
# def pickingNumbers(a):
#     # Write your code here
#     #count the instances of the integer in the array
#     from collections import Counter
#
#     a= ["4","6","5","3","3","1"]
#     count = Counter(a)
#     #get the integer count and the integer + 1 count if exists, else 0
#     #for the unique integers in the array
#
#     all_combos = [(count.get(k) + count.get(str(int(k) + 1),0)) for k in count.keys()]
#     #now all we need is the max value of the combos,
#     #keep in mind the combo can be just one integer!
#     print(max(all_combos))
#     return max(all_combos)

# if __name__ == '__main__':
#     #    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input().strip())
#
#     a = list(map(int, input().rstrip().split()))
#
#     result = pickingNumbers(a)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
# 6
# 4 6 5 3 3 1
###
#
# def climbingLeaderboard(scores, alice):
#     # List to contain and return Alice's ranks.
#     results = []
#
#     # Unique values from scores, since duplicate scores will have same rank (their index value).
#     leaderboard = sorted(set(scores), reverse = True)
#
#     # Use this var to track index within leaderboard later.
#     l = len(leaderboard)
#
#     # Loop through each of Alice's scores
#     for a in alice:
#
#         # If Alice's score is >= the score at the index of the end of leaderboard...
#         # Subtract 1 from that index value (which is also the rank) to check the next score up.
#         # If the score is less than the next score up, the index (rank) will be added to results.
#         while (l > 0) and (a >= leaderboard[l-1]):
#             l -= 1
#
#         # We add 1 to the appended value to account for 0-indexing.
#         results.append(l+1)
#
#     return results
#
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     scores_count = int(input())
#
#     scores = list(map(int, input().rstrip().split()))
#
#     alice_count = int(input())
#
#     alice = list(map(int, input().rstrip().split()))
#
#     result = climbingLeaderboard(scores, alice)
#
#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()

# 6
# 100 90 90 80 75 60
# 5
# 50 65 77 90 102


# def palindrome(word):
#     for i in range(len(word)//2):
#         if word[i] != word[-i-1]:
#             return False
#     return True

# print(palindrome("abcba"))


# Complete the hourglassSum function below.
# def hourglassSum(arr):
#     a = max([sum(arr[j][i:i+3]) + arr[j+1][i+1] + sum(arr[j+2][i:i+3])
#              for j in range(len(arr)-2) for i in range(len(arr[0])-1)] )
#     return a

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     arr = []
#
#     for _ in range(6):
#         arr.append(list(map(int, input().rstrip().split())))
#
#     result = hourglassSum(arr)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 2 4 4 0
# 0 0 0 2 0 0
# 0 0 1 2 4 0
#


# def leftrotate(n,d,a):
#     arr = [int(arr_t) for arr_t in a]
#     for _ in range(d):
#         arr.append(arr.pop(0))
#     print(*arr)
#
#     return arr


# if __name__ == '__main__':
#     nd = input().split()
#
#     n = int(nd[0])
#
#     d = int(nd[1])
#
#     a = input().rstrip().split()
#
#     leftrotate(n,d,a)


# 5 4
# 1 2 3 4 5
#


# Complete the arrayManipulation function below.

# def arrayManipulation(n, queries):
#     arr = [0]*(n+2)
#     for a, b, k in queries:
#         arr[a]+=k
#         arr[b+1]-=k
#     result = acc = 0
#     for x in arr:
#         acc+=x
#         result = max(result, acc)
#     return result

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     nm = input().split()
#
#     n = int(nm[0])
#
#     m = int(nm[1])
#
#     queries = []
#
#     for _ in range(m):
#         queries.append(list(map(int, input().rstrip().split())))
#
#     result = arrayManipulation(n, queries)
#
#     fptr.write(str(result) + '\n')
#
#     fptr.close()
# 5 3
# 1 2 100
# 2 5 100
# 3 4 100


# Returns true if there is a subset
# of set[] with sun equal to given sum
# def isSubsetSum(set,n, sum) :
#
#     # Base Cases
#     if (sum == 0) :
#         return True
#     if (n == 0 and sum != 0) :
#         return False
#
#     # If last element is greater than
#     # sum, then ignore it
#     if (set[n - 1] > sum) :
#         return isSubsetSum(set, n - 1, sum);
#
#         # else, check if sum can be obtained
#     # by any of the following
#     # (a) including the last element
#     # (b) excluding the last element
#     return isSubsetSum(set, n-1, sum) or isSubsetSum(set, n-1, sum-set[n-1])

# Other solutions
# A Dynamic Programming solution for subset sum problem
# Returns true if there is a subset of
# set[] with sun equal to given sum
#
# def isSubsetSum(set,n,sum):
#
#     # The value of subset[i][j] will be
#     # true if there is a
#     # subset of set[0..j-1] with sum equal to i
#     subset=([[False for i in range(sum+1)]
#              for i in range(n+1)])
#     # ([[False for i in range(10)]
#     #         for i in range(7)])
#     # If sum is 0, then answer is true
#     for i in range(n+1):
#         subset[i][0] = True
#
#         # If sum is not 0 and set is empty,
#         # then answer is false
#         for i in range(1,sum+1):
#             subset[0][i]=False
#
#         # Fill the subset table in botton up manner
#         for i in range(1,n+1):
#             for j in range(1,sum+1):
#                 if j<set[i-1]:
#                     subset[i][j] = subset[i-1][j]
#                     print(i,j,set[i-1], subset[i][j] ,subset[i-1][j] )
#                 if j>=set[i-1]:
#                     subset[i][j] = (subset[i-1][j] or
#                                     subset[i - 1][j-set[i-1]])
#
#
#
#                 #         uncomment this code to print table
#             #        for i in range(n+1):
#             #            for j in range(sum+1):
#             #                print (subset[i][j],end=" ")
#             #        print()
#         print (subset)
#     return subset[n][sum]
#
# # Driver program to test above function
# # if __name__=='__main__':
# #     set = [3, 34, 4, 12, 5, 2]
# #     sum = 9
# #     n =len(set)
# #     if (isSubsetSum(set, n, sum) == True):
# #         print("Found a subset with given sum")
# #     else:
# #         print("No subset with given sum")
#
#     # This code is contributed by
# # # sahil shelangia.
# # arr = set
# # array = set
# # num = sum
# #
# # def subset(array, num):
# #     result = []
# #     def find(arr, num, path=()):
# #         if not arr:
# #             return
# #         if arr[0] == num:
# #             result.append(path + (arr[0],))
# #         else:
# #             find(arr[1:], num - arr[0], path + (arr[0],))
# #             find(arr[1:], num, path)
# #     find(array, num)
# #     return result
# #
# # subset(array,num)
#
# #
# ##
#
# # Python3 code to demonstrate Difference Array
#
# # Creates a diff array D[] for A[] and returns
# # it after filling initial values.
# def initializeDiffArray( A):
#     n = len(A)
#
#     # We use one extra space because
#     # update(l, r, x) updates D[r+1]
#     D = [0 for i in range(0 , n + 1)]
#
#     D[0] = A[0]; D[n] = 0
#
#     for i in range(1, n ):
#         D[i] = A[i] - A[i - 1]
#     return D
#
#
# # Does range update
# def update(D, l, r, x):
#
#     D[l] += x
#     D[r + 1] -= x
#
#
# # Prints updated Array
# def printArray(A, D):
#
#     for i in range(0 , len(A)):
#         if (i == 0):
#             A[i] = D[i]
#
#             # Note that A[0] or D[0] decides
#         # values of rest of the elements.
#         else:
#             A[i] = D[i] + A[i - 1]
#
#         print(A[i], end = " ")
#
#     print ("")
#
#
# # # Driver Code
# # A = [ 10, 5, 20, 40 ]
# #
# # # Create and fill difference Array
# # D = initializeDiffArray(A)
# #
# # # After below update(l, r, x), the
# # # elements should become 20, 15, 20, 40
# # update(D, 0, 1, 10)
# # printArray(A, D)
# #
# # # After below updates, the
# # # array should become 30, 35, 70, 60
# # update(D, 1, 3, 20)
# # update(D, 2, 2, 30)
# # printArray(A, D)
# # printArray()
# # # This code is contributed by Gitanjali.
#
# ##
# # Time: O(nk) , Space: O(nk)
# def maxprofitwithktransactions(prices,k):
#     if not len(prices):
#         return 0
#     profit = [[0 for d in prices] for t in range(k+1)]
#     for t in range(1,k+1):
#         maxthusfar = float("-inf")
#         for d in range(1, len(prices)):
#             maxthusfar = max(maxthusfar, profit[t-1][d-1] - prices[d-1])
#             profit[t][d] = max(profit[t][d-1] , maxthusfar + prices[d])
#         return profit[-1][-1]
# #Time: O(nk), Space: O(n)
#
# def maxprofitwithktransaction(prices,k):
#     if not len(prices):
#         return 0
#     #        pritnt(80)
#     evenProfit = [0 for d in prices]
#     oddProfit = [0 for d in prices]
#     for t in range(1,k +1):
#         maxthusfar = float("-inf")
#         if t%2 == 1:
#             currentProfit = oddProfit
#             previousProfit = evenProfit
#         else:
#             currentProfit = evenProfit
#             previousProfit = oddProfit
#         for d in range(1, len(prices)):
#             maxthusfar = max(maxthusfar, previousProfit[d-1] - prices[d-1])
#             currentProfit[d] = max(currentProfit[d-1] ,maxthusfar + prices[d])
#     return evenProfit[-1] if k%2 == 0 else oddProfit[-1]
#
# # prices = [50,25,12,4,3,10,1,100]
# # k = 2
# #
# # maxprofitwithktransaction(prices,k)
#
#
# # Copyright © 2019 AlgoExpert, LLC. All rights reserved.
# # O(wh) time | O(wh) space
# def riverSizes(matrix):
#     sizes = []
#     visited = [[False for value in row] for row in matrix]
#     for i in range(len(matrix)):
#         for j in range(len(matrix[i])):
#             if visited[i][j]:
#                 continue
#             traverseNode(i, j, matrix, visited, sizes)
#     return sizes
#
# def traverseNode(i, j, matrix, visited, sizes):
#     currentRiverSize = 0
#     nodesToExplore = [[i, j]]
#     while len(nodesToExplore):
#         currentNode = nodesToExplore.pop()
#         i = currentNode[0]
#         j = currentNode[1]
#         if visited[i][j]:
#             continue
#         visited[i][j] = True
#         if matrix[i][j] == 0:
#             continue
#         currentRiverSize += 1
#         unvisitedNeighbors = getUnvisitedNeighbors(i, j, matrix, visited)
#         for neighbor in unvisitedNeighbors:
#             nodesToExplore.append(neighbor)
#     if currentRiverSize > 0 :
#         sizes.append(currentRiverSize)
#
# def getUnvisitedNeighbors(i, j, matrix, visited):
#     unvisitedNeighbors = []
#     if i > 0 and not visited[i - 1][j]:
#         unvisitedNeighbors.append([i - 1, j])
#     if i < len(matrix) - 1 and not visited[i + 1][j]:
#         unvisitedNeighbors.append([i + 1, j])
#     if j > 0 and not visited[i][j - 1]:
#         unvisitedNeighbors.append([i, j - 1])
#     if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
#         unvisitedNeighbors.append([i, j + 1])
#     return unvisitedNeighbors
#
# ### largestRange: find continuous range in Array.
#
# def largestRange(array):
#     bestRange = []
#     longestLength = 0
#     nums = {}
#     for num in array:
#         nums[num] = True
#     for num in array:
#         if not nums[num]:
#             continue
#         nums[num] = False
#         currentLength = 1
#         left = num - 1
#         right = num + 1
#         while left in nums:
#             nums[left] = False
#             currentLength += 1
#             left -= 1
#         while right in nums:
#             nums[right] = False
#             currentLength += 1
#             right += 1
#         if currentLength > longestLength:
#             longestLength = currentLength
#             bestRange = [left + 1, right - 1]
#     return bestRange
#
# ### Birthday chocolate
#
# # Complete the birthday function below.
# def birthday(s, d, m):
#     #return sum([1 for i in range(n-m+1) if sum(s[i:i+m]) == d])
#     return sum(1 for x in range(len(s)) if sum(s[x:x+m]) == d)
# #s: an array of integers, the numbers on each of the squares of chocolate
# #d: an integer, Ron's birth day
# #m: an integer, Ron's birth month
# #
# # if __name__ == '__main__':
# #     fptr = open(os.environ['OUTPUT_PATH'], 'w')
# #
# #     n = int(input().strip())
# #
# #     s = list(map(int, input().rstrip().split()))
# #
# #     dm = input().rstrip().split()
# #
# #     d = int(dm[0])
# #
# #     m = int(dm[1])
# #
# #     result = birthday(s, d, m)
# #
# #     fptr.write(str(result) + '\n')
# #
# #     fptr.close()
# #
#
# # Complete the reverseArray function below.
# def reverseArray(a):
#     return [str(x) for x in reversed(a)]
# #
# # if __name__ == '__main__':
# #     fptr = open(os.environ['OUTPUT_PATH'], 'w')
# #
# #     arr_count = int(input())
# #
# #     arr = list(map(int, input().rstrip().split()))
# #
# #     res = reverseArray(arr)
# #
# #     fptr.write(' '.join(map(str, res)))
# #     fptr.write('\n')
# #
# #     fptr.close()
#
# # Bisection Algorithm
#
# def bisection(f,a,b,N):
#     '''Approximate solution of f(x)=0 on interval [a,b] by bisection method.
#
#     Parameters
#     ----------
#     f : function
#         The function for which we are trying to approximate a solution f(x)=0.
#     a,b : numbers
#         The interval in which to search for a solution. The function returns
#         None if f(a)*f(b) >= 0 since a solution is not guaranteed.
#     N : (positive) integer
#         The number of iterations to implement.
#
#     Returns
#     -------
#     x_N : number
#         The midpoint of the Nth interval computed by the bisection method. The
#         initial interval [a_0,b_0] is given by [a,b]. If f(m_n) == 0 for some
#         midpoint m_n = (a_n + b_n)/2, then the function returns this solution.
#         If all signs of values f(a_n), f(b_n) and f(m_n) are the same at any
#         iteration, the bisection method fails and return None.
#
#     Examples
#     --------
#     >>> f = lambda x: x**2 - x - 1
#     >>> bisection(f,1,2,25)
#     1.618033990263939
#     >>> f = lambda x: (2*x - 1)*(x - 3)
#     >>> bisection(f,0,1,10)
#     0.5
#     '''
#     if f(a)*f(b) >= 0:
#         print("Bisection method fails.")
#         return None
#     a_n = a
#     b_n = b
#     for n in range(1,N+1):
#         m_n = (a_n + b_n)/2
#         f_m_n = f(m_n)
#         if f(a_n)*f_m_n < 0:
#             a_n = a_n
#             b_n = m_n
#         elif f(b_n)*f_m_n < 0:
#             a_n = m_n
#             b_n = b_n
#         elif f_m_n == 0:
#             print("Found exact solution.")
#             return m_n
#         else:
#             print("Bisection method fails.")
#             return None
#     return (a_n + b_n)/2
#
# # f = lambda x: x**2 - x - 1
# # approx_phi = bisection(f,1,2,25)
# #
# # error_bound = 2**(-26)
# # print(error_bound)
# #
# # abs( (1 + 5**0.5)/2 - approx_phi) < error_bound
#
# # Graph
#
# #!/bin/python3
# #
# # Complete the componentsInGraph function below.
# #
# def parent(parents, i):
#     if parents[i] != i:
#         parents[i] = parent(parents, parents[i])
#     return parents[i]
#
# def componentsInGraph(gb):
#     parents = list(range(len(gb)*2+1))
#
#     for a, b in gb:
#         #        print(parent(parents, a))
#         p1, p2 = parent(parents, a), parent(parents, b)
#         parents[p1] = parents[p2] = parents[a] = parents[b] = min(p1, p2)
#
#     print( parents)
#     counter = Counter()
#     for p in parents:
#         counter[parent(parents, p)]+=1
#         print( parent(parents, p))
#     counts = [c for c in counter.values() if c > 1]
#     return min(counts), max(counts)
#
# # componentsInGraph(gb)
# #
# # if __name__ == '__main__':
# #     #    fptr = open(os.environ['OUTPUT_PATH'], 'w')
# #
# #     os.environ['HOME'] = '/Users/petern/Desktop/Python/DataStructure/graph.txt'
# #
# #     fptr = open(os.environ['HOME'], 'w')
# #
# #     n = int(input())
# #
# #     gb = []
# #
# #     for _ in range(n):
# #         gb.append(list(map(int, input().rstrip().split())))
# #
# #     result = componentsInGraph(gb)
# #
# #     componentsInGraph(gb)
# #
# #     fptr.write(str(result))
# #
# #     fptr.close()
# #
# #     myfile = open(os.environ['HOME'],'r')
# #
# #     print((myfile.readlines()))
# #    fptr.write(' '.join(map(str,result )))
# #    fptr.write('\n')
# #
# #    fptr.close()
#
# # Enter your code here. Read input from STDIN. Print output to STDOUT
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.parent = self
#         self.rank = 0
#         self.size = 1
#
# class DSF:
#     @staticmethod
#     def make_set(data):
#         return Node(data)
#
#     @staticmethod
#     def find(node):
#         if node != node.parent:
#             node.parent = DSF.find(node.parent)
#         return node.parent
#
#     @staticmethod
#     def union(node_a, node_b):
#         root_a = DSF.find(node_a)
#         root_b = DSF.find(node_b)
#
#         if root_a != root_b:
#             if root_a.rank > root_b.rank:
#                 root_b.parent = root_a
#                 root_a.size += root_b.size
#             else:
#                 root_a.parent = root_b
#                 root_b.size += root_a.size
#                 if root_a.rank == root_b.rank:
#                     root_b.rank += 1
#
# # N, Q = map(int, input().split())
# # people = [DSF.make_set(i) for i in range(1, N+1)]
# # outputs = []
# #
# # for _ in range(Q):
# #     inputs = input().split()
# #     if inputs[0] == 'Q':
# #         I = int(inputs[1])
# #         outputs.append(DSF.find(people[I-1]).size)
# #     elif inputs[0] == 'M':
# #         I, J = map(int, inputs[1:])
# #         DSF.union(people[I-1], people[J-1])
# #
# # for query in outputs:
# #     print(query)
#
# # Kunno And Tree
# # https://math.stackexchange.com/questions/838792/counting-triplets-with-red-edges-in-each-pair?newreg=60eee35f0b3844de852bda39f6dfec88
# class DisjointSet:
#
#     def __init__(self, N):
#         self.parent = [i for i in range(N)]
#         self.total = [1] * N
#
#     def union(self, a, b):
#         a_parent = self.find(a)
#         b_parent = self.find(b)
#         if a_parent != b_parent:
#             self.parent[b_parent] = a_parent
#             self.total[a_parent] += self.total[b_parent]
#
#     def find(self, a):
#         if self.parent[a] != a:
#             self.parent[a] = self.find(self.parent[a])
#         return self.parent[a]
#
#     def get_total(self, a):
#         return self.total[self.find(a)]
# #
# # N = int(input())
# # ds = DisjointSet(N)
# # for i in range(N - 1):
# #     x, y, color = input().split()
# #     if color == 'b':
# #         ds.union(int(x) - 1, int(y) - 1)
# # set_size = {ds.find(i): ds.get_total(i) for i in range(N)}
# # complement = sum(x * (x - 1) * (N - x) // 2 +              #1
# #                  x * (x - 1) * (x - 2) // 6                #2
# #                  for x in set_size.values())
# # print((N * (N - 1) * (N - 2) // 6 - complement) % (10 ** 9 + 7))
#
#
#
# # super maximum cost query
# # Complete the solve function below.
#
# # from bisect import bisect_left,bisect_right
# # parents = {}
# # rep = {}
# def make_set(n):
#     global parents,rep
#     parents=dict(zip(range(1,n+1),range(1,n+1)))
#     rep=dict(zip(range(1,n+1),({i} for i in range(1,n+1))))
#
# def add_edge(x, y,paths,w):
#     xroot = find(x)
#     yroot = find(y)
#     paths[w]+=len(rep[xroot])*len(rep[yroot])
#     if xroot == yroot:
#         return
#     else:
#         if len(rep[yroot])<len(rep[xroot]):
#             parents[yroot] = xroot
#             rep[xroot].update(rep[yroot])
#             del rep[yroot]
#         else:
#             parents[xroot] = yroot
#             rep[yroot].update(rep[xroot])
#             del rep[xroot]
#
# def find(x):
#     if parents[x] != x:
#         parent = find(parents[x])
#         parents[x] = parent
#     return parents[x]
#
# def solve(tree, queries):
#     n = len(tree)+1
#     tree.sort(key=lambda e:e[2])
#     paths = {0:0}
#     weights = [0]
#     prev = 0
#     make_set(len(tree)+1)
#     for a,b,w in tree:
#         if w != prev:
#             weights.append(w)
#             paths[w] = paths[prev]
#         add_edge(a,b,paths,w)
#         prev=w
#     for l,r in queries:
#         wr = weights[bisect_right(weights,r)-1]
#         wl = weights[bisect_right(weights,l-1)-1]
#         yield paths[wr]-paths[wl]
# #
# # if __name__ == '__main__':
# #     fptr = open(os.environ['OUTPUT_PATH'], 'w')
# #
# #     nq = input().split()
# #
# #     n = int(nq[0])
# #
# #     q = int(nq[1])
# #
# #     tree = []
# #
# #     for _ in range(n-1):
# #         tree.append(list(map(int, input().rstrip().split())))
# #
# #     queries = []
# #
# #     for _ in range(q):
# #         queries.append(list(map(int, input().rstrip().split())))
# #
# #     result = solve(tree, queries)
# #
# #     fptr.write('\n'.join(map(str, result)))
# #     fptr.write('\n')
# #
# #     fptr.close()
#
# #5 5
# #1 2 3
# #1 4 2
# #2 5 6
# #3 4 1
# #1 1
# #1 2
# #2 3
# #2 5
# #1 6
#
# #Another solution to super
#
# # Complete the solve function below.
#
# #!/bin/python3
#
#
# class disjoint_set:
#     class Node:
#         def __init__(self, data = 0):
#             self.data = data
#             self.parent = self
#             self.rank = 0
#             self.size = 1
#
#     def __init__(self):
#         self.items = dict()
#         self.ans = 0
#
#     def make_set(self, data):
#         if not data in self.items:
#             self.items[data] = self.Node(data)
#         return self.items
#
#     def find_set(self, data):
#         if data in self.items:
#             node = self.items[data]
#         else:
#             return False
#
#         if node.parent == node:
#             return node
#         node.parent = self.find_set(node.parent.data)
#
#         return node.parent
#
#     def union(self, rep1, rep2):
#         node1 = self.find_set(rep1)
#         node2 = self.find_set(rep2)
#
#         #print("union: node1 = {} node2 = {}".format(node1.data, node2.data))
#
#         if node1 and node2 and node1 != node2:
#             if node1.rank >= node2.rank:
#                 if node1.rank == node2.rank:
#                     node1.rank += 1
#                 self.ans -= (node1.size*(node1.size - 1))//2 + (node2.size*(node2.size - 1))//2
#                 node2.parent = node1
#                 node1.size += node2.size
#                 self.ans += (node1.size*(node1.size - 1))//2
#             else:
#                 self.ans -= (node1.size*(node1.size - 1))//2 + (node2.size*(node2.size - 1))//2
#                 node1.parent = node2
#                 node2.size += node1.size
#                 self.ans += (node2.size*(node2.size - 1))//2
#         return True
#
#     def get_size(self, rep):
#         return self.find_set(rep).size
#
#     def get_ans(self):
#         return self.ans
#
# # Complete the solve function below.
# def solve(tree, queries):
#     dset = disjoint_set()
#     tree = sorted(tree, key=lambda x: x[2])
#     weights = list(map(lambda x: x[2], tree))
#     anses = []
#
#     for el in tree:
#         dset.make_set(el[0])
#         dset.make_set(el[1])
#         dset.union(el[0], el[1])
#
#         anses.append(dset.get_ans())
#         print("adding {} ans = {}".format(el, dset.get_ans()))
#
#     print("weights: {} anses: {}".format(weights, anses))
#     # do queries
#     output = []
#     for q in queries:
#         qleft, qright = q[0], q[1]
#
#         if qright < weights[0]:
#             output.append(0)
#         else:
#             right = bisect_right(weights, qright) - 1
#             print("query: {} RIGHT weights[{}] = {}".format(q, right, weights[right]))
#
#             if qleft <= weights[0]:
#                 output.append(anses[right])
#             else:
#                 left = bisect_left(weights, qleft) - 1
#                 print("query: {} LEFT weights[{}] = {}".format(q, left, weights[left]))
#                 output.append(anses[right] - anses[left])
#
#
#     return output
# #
# # if __name__ == '__main__':
# #     os.environ['HOME'] = '/Users/petern/Desktop/Python/DataStructure/graph_supersum.txt'
# #
# #     fptr = open(os.environ['HOME'], 'w')
# #
# #     nq = input().split()
# #
# #     n = int(nq[0])
# #
# #     q = int(nq[1])
# #
# #     tree = []
# #
# #     for _ in range(n-1):
# #         tree.append(list(map(int, input().rstrip().split())))
# #
# #     queries = []
# #
# #     for _ in range(q):
# #         queries.append(list(map(int, input().rstrip().split())))
# #
# #     result = solve(tree, queries)
# #
# #     fptr.write(str(result))
# #
# #     fptr.close()
# #
# #     myfile = open(os.environ['HOME'],'r')
# #
# #     print((myfile.readlines()))
#
# #
# # Complete the minimumAverage function below.
#
# def minimumAverage(cust):
#     lenCust = len(cust)
#     if lenCust == 0: return 0
#     heapify(cust)
#     tlWait = 0
#     done = 0
#     orders = []
#
#     while orders or cust:
#         while ((not cust) or done < cust[0][0]) and orders:
#             (dw, dt) = heappop(orders)
#             done = dw + max(done, dt)
#             tlWait += done - dt
#         if (cust): heappush(orders, heappop(cust)[::-1])
#
#     return tlWait // lenCust
#
# # if __name__ == '__main__':
# #
# #     os.environ['HOME'] = '/Users/petern/Desktop/Python/DataStructure/graph_minimum.txt'
# #
# #     fptr = open(os.environ['HOME'], 'w')
# #
# #     n = int(input())
# #
# #     customers = []
# #
# #     for _ in range(n):
# #         customers.append(list(map(int, input().rstrip().split())))
# #
# #
# #     result = minimumAverage(customers)
# #
# #     fptr.write(str(result))
# #
# #     fptr.close()
# #
# #     myfile = open(os.environ['HOME'],'r')
# #
# #     print((myfile.readlines()))
#
#     # 3
#     # 0 3
#     # 1 9
#     # 2 5
#
# # # O(N^2) setup, O(N) per query.
# # # This is not properly factored into functions, sorry.
# #
# # N, K = map(int, input().split(' '));  # N = #sumos, K = allowable height difference.
# # heights = list(map(int, input().split(' ')))  # Height of wrestler by index.
# # assert N == len(heights);
# #
# # fights = [[0] for i in range(N)];
# # # fights[i][j] = Number of fights allowed between sumo i and sumo i+1 through i+j
# # for sumo1, height1 in enumerate(heights):
# #     num_fights = 0;
# #     for sumo2 in range(sumo1 + 1, N):
# #         if abs(height1 - heights[sumo2]) <= K: num_fights += 1;
# #         fights[sumo1].append(num_fights);
#
#
# def query(l, r):  # l = lower index, r = upper
#     "Determines the number of allowable fights between sumos in index range l to r."
#     return sum(fights[sumo][r - sumo] for sumo in range(l, r));
#
#
# def run_queries():
#     num_queries = int(input());
#     for i in range(num_queries):
#         if i: print("")
#         l, r = map(int, input().split(' '));
#         print(query(l, r), end="");
#
#
# # run_queries();
#
# # 5 2
# # 1 3 4 3 0
# # 3
# # 0 1
# # 1 3
# # 0 4
#
