from graphInput import *
from copy import deepcopy as copy
# sample larger #

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

	for e in removed:
		esm = edges.index(e)
		scoreList[esm] += score

	return

gBest = 0
gBestPath = []
particles = []
particleScore = []

for i in range(150):
	path = randomEdges(B, edges)
	particles.append(path)
	fit = fitness(graph, path, infected)
	particleScore.append(fit)

	if fit > gBest: # exchange with group best
		gBest = fit
		gBestPath = path

lenPart = len(particles)
vSize = 2
indSize = 2
cSize = 2
weightSum = vSize+indSize+cSize
stepSize = 1

probOfInd = float(indSize)/ weightSum
probOfCog = float(cSize)/ weightSum
probOfvolec = float(vSize) / weightSum

for i in range(100):
	grpBest = []
	for particle in range(lenPart):
		theLen = len(particles[particle])
		vPath = randomEdges(theLen,edges)

        sigleBestPath = random.sample(particles[particle], int(probOfInd*theLen*stepSize))
        grpBestPath = random.sample(gBestPath, int(probOfCog*theLen*stepSize))
        vlcBestPath = random.sample(vPath, int(probOfCog*theLen*stepSize))
        
        print("s", sigleBestPath)
        print("g", grpBestPath)
        print("v", vlcBestPath)
        
        sigleBestPath[len(sigleBestPath):] = grpBestPath
        sigleBestPath[len(sigleBestPath):] = vlcBestPath

        fromLastParticle = len(particles[particle]) - len(sigleBestPath)
        last = random.sample(particles[particle], fromLastParticle)
        
        sigleBestPath[len(sigleBestPath):] = last
        sigleBestPath = list(set(sigleBestPath))
        fromLastParticle = len(particles[particle]) - len(sigleBestPath)
        last = random.sample(particles[particle], fromLastParticle)
        sigleBestPath[len(sigleBestPath):] = last

        print(sigleBestPath)
        print('===================================================================')

        fitt = fitness(graph, sigleBestPath, infected)

        if fitt < particleScore[particle]: # better fitness
        	particleScore[particle] = fitt
        	particles[particle] = sigleBestPath

        if fitt < gBest:
        	gBest = fitt
        	gBestPath = sigleBestPath

        grpBest.append(gBest)

	plt.plot(range(len(grpBest)),grpBest)
	print(grpBest)


print(gBestPath, gBest)
