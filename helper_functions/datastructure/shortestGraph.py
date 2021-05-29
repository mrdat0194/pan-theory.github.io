#!/bin/python3

import os


# Complete the findShortest function below.
# idx is color for nodes, find path between 2 same color =  same val
#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
# 
from collections import defaultdict
from queue import Queue

from queue import Queue
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    g = {i + 1: [] for i in range(graph_nodes)}
    for i in range(len(graph_from)):
        g[graph_from[i]].append(graph_to[i])
        g[graph_to[i]].append(graph_from[i])

    target_nodes = []

    for i in range(len(ids)):
        if ids[i] == val:
            target_nodes.append(i + 1)
    result = -1
    for node in target_nodes:
        w = weight(g, target_nodes, node, result)
        if w >0 and w < result or result == -1:
            result = w
    return result

def weight(g, target_nodes, node, limit=-1):
    visited = set()
    q = Queue()
    q.put((node, 0))
    while not q.empty():
        n, w = q.get()
        if n in visited:
            continue
        if n in target_nodes and n != node:
            return w
        visited.add(n)
        if w == limit:
            return -1
        for next_node in g[n]:
            if next_node not in visited:
                q.put((next_node, w + 1))
    return -1

# class Graph:
#     def __init__(self):
#         self.edge_map = defaultdict(set)
    
#     def connect(self, from_, to_):
#         self.edge_map[from_].add(to_)
#         self.edge_map[to_].add(from_)
    
#     def shortest_path_from(self, start_node, cond):
#         visited = set()
#         q = Queue()
#         q.put([start_node, 0])
#         visited.add(start_node)
        
#         while not q.empty():
#             source, dist = q.get()
            
#             for neighbor in self.edge_map[source]:
#                 if not neighbor in visited:
#                     if cond(neighbor): return dist+1

#                     q.put([neighbor, dist+1])
#                     visited.add(neighbor)

#         return -1

# def add_edges(graph, graph_from, graph_to):
#     for i in range(len(graph_from)):
#         from_ = graph_from[i]
#         to_ = graph_to[i]
#         graph.connect(from_, to_)

# def findShortest(graph_nodes, graph_from, graph_to, ids, val):
#     color_to_match = ids[val-1]
    
#     g = Graph()
#     add_edges(g, graph_from, graph_to)
#     return g.shortest_path_from(val, lambda node: ids[node-1] == color_to_match)

#5 4
#1 2
#1 3
#2 4
#3 5
#1 2 3 3 2
#2

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    output = os.path.join(BASE_DIR, "Shortest_Graph.txt")
    if os.path.exists(output):
        f = open(output, "r+")
    else:
        f = open(output, "w")

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    f.write(str(ans) + '\n')

    f.close()

