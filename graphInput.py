import random
import itertools
from collections import defaultdict

v = 20 #vertices 
I = 10 #infected nodes
e = 200 #edges
B = 100 #budget
maxD = 0 #max degree (0 for no limit)

nodes = set()
graph = defaultdict()

myFile = open('input.txt', 'w')
for i in range(0,v): #vertices
    nodes.add(i) 
    graph[i] = []

edges = random.sample(
    list(itertools.combinations(nodes, 2)),
    len(list(itertools.combinations(nodes,2)))
    )
random.shuffle(edges)

for edge in edges: # edges
    if e > 0:
        if (maxD != 0) and (len(graph) > 0):
            if len(graph[edge[0]]) >= maxD:
                continue
            if len(graph[edge[1]]) >= maxD:
                continue
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

        myFile.write(str(edge[0]) + ' ' + str(edge[1]) + '\n')
        e = e - 1
    else:
        break

myFile.close()

if I<v: # check infected
    u = random.sample(nodes, I)
    infected = {n for n in u}
else:
    print('infected nodes number are not correct')

removed = set() # removed set
