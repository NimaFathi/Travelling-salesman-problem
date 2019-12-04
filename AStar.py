from heapq import *
import numpy as np

# Kruskal algorithm implementation:
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


# A star algorithm implementation

def astar(array, start, goal, n):
    close_set = set()
    came_from = {}
    gscore = {start: 0}
    minInRowone = np.amin(array[0][1:])  # min in first row for starting fscore
    # starting Kruskal:
    kruskalLen = 0
    my_list = list()
    my_set = set()
    for i in range(1, n):
        my_list.append(i)
        for j in range(1, i):
            if arr[i][j] == -1:
                continue
            my_set.add((arr[i][j], i, j))
    graph = {
        'vertices': list(my_list),
        'edges': set(my_set)
    }
    my_tuple = tuple(kruskal(graph))

    for i in range(len(my_tuple)):
        kruskalLen += my_tuple[i][0]
    hstart = 2 * minInRowone + kruskalLen
    came_from[start] = None
    fscore = {start: hstart}
    oheap = []
    data = []
    heappush(oheap, (fscore[start], start))
    # Do A start until oheap have members in it :
    while oheap:
        while True:
            ans, current = heappop(oheap)
            if current in close_set:
                continue
            else:
                break
        data.append(current + 1)
        close_set.add(current)
        currentNum = len(close_set)

        # return condition:
        if currentNum == goal:
            return data, ans

        # Kruskal setting ...
        my_set = set()
        my_list = list()
        for k in range(n):
            for j in range(k):
                if k not in close_set:
                    my_list.append(k)
                    if j not in close_set:
                        my_set.add((array[k][j], k, j))
        graph = {
            'vertices': list(my_list),
            'edges': set(my_set)
        }

        my_tuple = tuple(kruskal(graph))
        kruskalLen = 0
        for k in range(len(my_tuple)):
            kruskalLen += my_tuple[k][0]

        # Nearest neighbor from current neighbor:
        min = float("inf")
        minindex = -1
        for i in range(n):
            if i not in close_set:
                if i != current:
                    if array[current][i] < min:
                        min = array[current][i]
                        minindex = i

        minstart = float("inf")
        minstartIndex = -1
        for k in range(n):
            if k not in close_set:
                if k != current:
                    if (array[start][k] < minstart):
                        minstartIndex = k
                        minstart = array[start][k]
        # Iterating over all possible neighbors:
        for i in range(0, n):
            neighbor = i
            if neighbor in close_set:
                continue
            # Kruskal setting ...
            my_set = set()
            my_list = list()
            for k in range(n):
                if k not in close_set and k != neighbor:
                    my_list.append(k)
                    for j in range(k):
                        if j not in close_set and j != neighbor and j != k:
                            my_set.add((array[k][j], k, j))
            graph = {
                'vertices': list(my_list),
                'edges': set(my_set)
            }

            my_tuple = tuple(kruskal(graph))
            kruskalLen = 0
            for k in range(len(my_tuple)):
                kruskalLen += my_tuple[k][0]

            # nearest unseen from neighbor :
            min = float("inf")
            minindex = -1
            for j in range(n):
                if j not in close_set and j != neighbor:
                    if (array[neighbor][j] < min):
                        min = array[neighbor][j]
                        minindex = j

            # nearest unseen from start IN this node
            minstart = float("inf")
            minstartIndex = -1
            for k in range(n):
                if k not in close_set and k != neighbor:
                    if (array[start][k] < minstart):
                        minstartIndex = k
                        minstart = array[start][k]

            # heuristic function:

            if minindex == -1:
                if minstartIndex == -1:
                    h = kruskalLen
                else:
                    h = minstart + kruskalLen
            else:
                if minstartIndex == -1:
                    h = min + kruskalLen
                else:
                    h = min + minstart + kruskalLen

            # print('current = ',current,' neighbor = ', neighbor)
            # print('min', min)
            # print('minstart',minstart)
            # print('h', h)

            tentative_g_score = gscore[current] + array[current][neighbor]
            # print(oheap)
            if neighbor in [i[1] for i in oheap]:
                # if gscore.get(neighbor, 0) > tentative_g_score:
                #   gscore[neighbor] = tentative_g_score
                #  fscore[neighbor] = tentative_g_score + h
                # heappush(oheap, (fscore[neighbor], neighbor))
                # came_from[neighbor] = current
                if fscore.get(neighbor, 0) > tentative_g_score + h:
                    fscore[neighbor] = tentative_g_score + h
                    came_from[neighbor] = current
                    heappush(oheap, (fscore[neighbor], neighbor))

            else:
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + h
                heappush(oheap, (fscore[neighbor], neighbor))
                came_from[neighbor] = current
    return data


# Driver code


n = int(input())
arr = np.empty((0, n), int)
for i in range(n):
    inputs = tuple(map(int, input().split()))
    arr = np.append(arr, np.array([inputs]), axis=0)
data = []
ans = 0
data, ans = astar(arr, 0, n, arr.shape[0])
x = 0
for i in range(n):
    if i == n - 1:
        x += arr[data[i] - 1][0]
    else:
        x += arr[data[i] - 1][data[i + 1] - 1]
print(x)
print(data)
