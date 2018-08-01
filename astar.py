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


def fitness(graph, removed, infected): # single removed edge is passed
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
	
	return sus, inpGraph # two returns

fit = []	
path = []
Min = 10*10

while B:
	for edge in edges:
		f, g = fitness(g, edge, infected)
		fit.append(f)

	Min = min(fit)
	path.append(edges.pop(fit.index(Min))) # path is made by min fitness 
	B -= 1

print(Min, path)
