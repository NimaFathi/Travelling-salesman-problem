import numpy as np
parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)

    minimum_spanning_tree = set()
    edges = list(graph['edges'])
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree

graph = {
        'vertices': [],
        'edges': set([
            ])
        }
my_list = list()

print(type(graph['vertices']))
print(type(graph['edges']))
my_set = set()
n = int(input())
arr = np.empty((0, n), int)
for i in range(n):
    my_list.append(i)
    inputs = tuple(map(int, input().split()))
    for j in range(n):
        arr = np.append(arr, np.array([inputs]), axis=0)
for i in range(n):
    for j in range(i):
        if arr[i][j] == -1:
            continue
        my_set.add(( arr[i][j],i, j))
graph = {
    'vertices': list(my_list),
    'edges': set(my_set)
}

minimum_spanning_tree = set([
            (1, 'A', 'B'),
            (2, 'B', 'D'),
            (1, 'C', 'D'),
            ])
my_tuple = tuple(kruskal(graph))
kruskalLen = 0
for i in range(len(my_tuple)):
    kruskalLen += my_tuple[i][0]
print(kruskalLen)
