from graphInput import *
from copy import deepcopy as copy

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


def randomEdges(n, edges):
	if n <= len(edges):
		e = random.sample(edges, n)
	else:
		while n > len(edges):
			n -= 1
		e = random.sample(edges, n)

	return e #list


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
	inpGraph = copy(list(graph.values()))
	inpRemoved = list(set(removed))
	inpInfected = list(infected)

	for x in inpRemoved:
		u , v = x
		inpGraph[u].pop(inpGraph[u].index(v))
		inpGraph[v].pop(inpGraph[v].index(u))

	sus = susCounter(inpGraph, inpInfected)

	for x in inpRemoved:
		u, v = x
		inpGraph[u].append(v)
		inpGraph[v].append(u)

	return sus

scoreList = [0 for i in range(len(edges))]

def scoredList(graph, removed, infected):
	score = fitness(graph, removed, infected)

	for e in removed: #score as fremon
		esm = edges.index(e)
		scoreList[esm] += score

	return


for i in range(150):
	path = randomEdges(B,edges)
	scoredList(graph, path, infected)

sumation = sum(scoreList)
namak = []

for i in range(20):
	while len(namak) < B:
		path = random.sample(edges,1)
		index = edges.index(path[0])

		if float(sumation) == 0:
			sumation += 1
		if float(scoreList[index])/float(sumation) < random.random():
			namak.extend(path)

	scoredList(graph, namak, infected)
	print(namak, fitness(graph, namak, infected))
	namak = []

	
