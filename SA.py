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


def randomEdges(n, edges):
	return random.sample(edges, n)


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
	inpGraph = list(graph.values())
	inpRemoved = list(removed)
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
	

isremoved = set()

for i in range(100):
	print('############    THIS IS THE ' + str(i) + 'th SET ATTEMPT    ############')

	randEdge = randomEdges(random.randrange(1, B+1), edges)
	removed = {i for i in randEdge}
	best = fitness(graph, removed, infected)
	rbest = len(removed)
	lfit = []

	print('----> INITIAL bestST FITNESS IS: ' + str(best))

	for j in range(100):#in set
		print('######    THIS IS THE ' + str(j) + 'th ATTEMPT    ######')
		
		prob = 1/(j+1) # SA probability
		p = random.choice([0,1])

		if p:
			if B < len(edges):
				added = randomEdges(random.randrange(1,B+1),edges)
				isremoved = {e for e in added}

				recbest = fitness(graph, isremoved, infected)
				rrecbest = len(isremoved)

				if recbest > best and random.random() < prob: # first accept more worst case senarios
					best = recbest
					removed = isremoved

				elif recbest < best:
					best = recbest
					removed = isremoved

				elif  recbest == best:

					if rrecbest < rbest:
						removed = isremoved

					if rrecbest == rbest:
						pr = random.choice([0,1])
						if pr:
							removed = isremoved

		if not p:

			if len(removed)>0:
				lremoved = random.sample(removed, random.randint(1,len(removed)))
				recbest = fitness(graph, lremoved, infected)
				rrecbest = len(lremoved)

				if recbest > best and random.random() < prob: # first accept more worst case senarios
					best = recbest
					removed = isremoved

				elif recbest <= best:
					best = recbest
					removed = lremoved
                    
		print('----> CURRENT BEST FITNESS IS: ' + str(best))
		lfit.append(best)

	plt.plot(range(len(lfit)),lfit)
