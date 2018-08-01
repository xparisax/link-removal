from graphInput import *

# as before
myFile = list(open('input.txt', 'r'))
edge = []
edges = []
for line in myFile:
    edge.append(line)
    edge = [x.strip() for x in edge]
for i in range(len(edge)):
    u, v = edge[i].split()
    edges.append((int(u),int(v)))

g = list(graph.values())


def susCounter(graph, infected):
    inf = list(infected)
    gf = list(graph)
    susReturn = 0

    for i in xrange(0, len(inf)):
        susReturn += len(graph[inf[i]]) 
        for j in xrange(0, len(graph[inf[i]])):
            checker = graph[inf[i]][j]
            susReturn += len(graph[checker]) 
    
    return susReturn


def fitness(graph, removed, infected):
    inpGraph = graph
    inpRemoved = list(removed)
    inpInfected = list(infected)

    u = inpRemoved[0]
    v = inpRemoved[1]
    inpGraph[u].pop(inpGraph[u].index(v))
    inpGraph[v].pop(inpGraph[v].index(u))

    sus = susCounter(inpGraph, inpInfected)

    inpGraph[u].append(v)
    inpGraph[v].append(u)

    return sus, inpGraph

path = []

def dfs(graph, edges, itrController, infected):
    if itrController != 0: # iteration
        for edge in edges:
            nowFitness, graph = fitness(graph, edge, infected)
            print(nowFitness)
            path.append(edges.pop(0))

            if nowFitness < len(infected)* 6000:# in rate bayad avaz she
                print("The Answer", path,"and Fitness is :", nowFitness)

                if(len(path)>=1):
                    temp = path.pop()
                    edges.append(temp)
            else: # not good enough
                dfs(graph,edges,itrController-1, infected)
                if(len(path)>=1):
                    temp = path.pop()
                    edges.append(temp)

for i in range(B):# iteration
    dfs(graph, edges, i+1, infected)
    path = []
