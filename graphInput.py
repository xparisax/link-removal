import random
import itertools
from collections import defaultdict

v = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))
maxD = int(input("Enter max degree (0 for no limit): "))

nodes = []
graph = defaultdict()

myFile = open('input.txt', 'w')
for i in range(1,v+1):
    myFile.write(str(i) + '\n')
    nodes.append(i)
    graph[i] = []

edges = random.sample(
    list(itertools.combinations(nodes, 2)),
    len(list(itertools.combinations(nodes,2)))
    )
random.shuffle(edges)

for edge in edges:
    if e > 0:
        if (maxD != 0) and (len(graph) > 0):
            if len(graph[edge[0]]) >= maxD:
                continue
            if len(graph[edge[1]]) >= maxD:
                continue
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
        myFile.write(str(edge[0]) + ',' + str(edge[1]) + '\n')
        e = e - 1
    else:
        break