#!/bin/python3

import os

def DFSrec(adj,s,visited,val):
    visited[s] = 1
    val += 1
    for i in adj[s]:
        if visited[i]==0:
            val = DFSrec(adj,i,visited,val)
    return val

def roadsAndLibraries(n, c_lib, c_road, cities):
    '''
    Return total cost
    https://www.hackerrank.com/challenges/torque-and-development/problem
    STDIN       Function
-----       --------
2           q = 2
3 3 2 1     n = 3, cities[] size m = 3, c_lib = 2, c_road = 1
1 2         cities = [[1, 2], [3, 1], [2, 3]]
3 1
2 3
6 6 2 5     n = 6, cities[] size m = 6, c_lib = 2, c_road = 5
1 3         cities = [[1, 3], [3, 4],...]
3 4
2 4
1 2
2 3
5 6
    :param n: number of road can be built
    :param c_lib: cost of library
    :param c_road: cost of road building
    :param cities: road can be built between cities
    :return:
    '''
    print("n",n)
    print("c_lib",c_lib)
    print("c_road",c_road)
    print("cities",cities)

    if c_road > c_lib:
        return n * c_lib
    else:

        ##adjacency matrix construction
        adj = dict()
        for i in cities:
            if i[0] in adj:
                adj[i[0]].append(i[1])
            else:
                adj[i[0]] = [i[1]]

            if i[1] in adj:
                adj[i[1]].append(i[0])
            else:
                adj[i[1]] = [i[0]]

        for i in range(1,n+1):
            if i in adj:
                pass
            else:
                adj[i] = []


        ##algorithm
        visited = [0]*(n+1)

        countNodes = 0
        countComponents = 0

        l = []
        for i in range(1,n+1):
            if visited[i]==0:
                val = 0
                nodes = DFSrec(adj,i,visited,val)
                countComponents += 1
                l.append(nodes)

        total = 0
        for i in l:
            total = total + (c_road*(i-1))

        total = total + countComponents*c_lib

        return total

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    output = os.path.join(BASE_DIR, "roadLibrary.txt")
    if os.path.exists(output):
        f = open(output, "r+")
    else:
        f = open(output, "w")

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        f.write(str(result) + '\n')

    f.close()

# 2
# 3 3 2 1
# 1 2
# 3 1
# 2 3
# 6 6 2 5
# 1 3
# 3 4
# 2 4
# 1 2
# 2 3
# 5 6