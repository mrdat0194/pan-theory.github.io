import queue
from collections import defaultdict

class Graph:
    '''
    Find all the distance from starting node
    starting node: 2
    Edge append

    1
    4 2
    1 2
    1 3
    1
    '''
    def __init__(self, n):
        self.n = n
        self.edges = defaultdict(lambda: [])

    def connect(self,x,y):
        self.edges[x].append(y)
        self.edges[y].append(x)

    def find_all_distances(self, root):
        distances = [-1 for i in range(self.n)]
        unvisited = set([i for i in range(self.n)])
        q = queue.Queue()
        distances[root] = 0
        unvisited.remove(root)
        q.put(root)

        while not q.empty():
            node = q.get()
            # print(distances)
            children = self.edges[node]
            height = distances[node]
            for child in children:
                if child in unvisited:
                    distances[child] = height + 6
                    unvisited.remove(child)
                    q.put(child)
        distances.pop(root)
        print(" ".join(map(str,distances)))

if __name__ == "__main__":

    t = int(input())
    for i in range(t):
        # Number of node and number of edge
        n,m = [int(value) for value in input().split()]
        graph = Graph(n)
        for i in range(m):
            x,y = [int(x) for x in input().split()]
            graph.connect(x-1,y-1)
        s = int(input())
        graph.find_all_distances(s-1)
