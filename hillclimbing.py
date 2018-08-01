from graphInput import *

myFile = list(open('input.txt', 'r'))
#read edges from file
edge = []
edges = []
for line in myFile:
	edge.append(line)
	edge = [x.strip() for x in edge]
for i in range(len(edge)):
	u, v = edge[i].split()
	edges.append((int(u),int(v)))

# random edge
def randomEdges(n, edges):
	return random.sample(edges, n)

#susceptible count: neighbour and its neighbours
def susCounter(graph, infected):
	inf = list(infected)
	gf = list(graph)
	susReturn = 0

	for i in xrange(0, len(inf)):
		susReturn += len(graph[inf[i]])
		# len(graph[inf[i]]) : Neighbours of infected node
		for j in xrange(0, len(graph[inf[i]])):
			#trace on each neighbour for add # Of them
			checker = graph[inf[i]][j]
			susReturn += len(graph[checker])

	return susReturn

def fitness(graph, removed, infected):
	inpGraph = list(graph.values())
	inpRemoved = list(removed)
	inpInfected = list(infected)

	for x in inpRemoved: #removed is as [(2,3),...]
		u , v = x
		inpGraph[u].pop(inpGraph[u].index(v)) # delete from sample grath
		inpGraph[v].pop(inpGraph[v].index(u))

	sus = susCounter(inpGraph, inpInfected)

	for x in inpRemoved: # add edges back in sample graph
		u, v = x
		inpGraph[u].append(v)
		inpGraph[v].append(u)
	
	return sus
	

isremoved = set() #set to be removed

for i in range(100):#different sets
	print('############    THIS IS THE ' + str(i) + 'th SET ATTEMPT    ############')

	randEdge = randomEdges(random.randrange(1, B+1), edges) #initial in-set
	removed = {i for i in randEdge}
	best = fitness(graph, removed, infected)
	rbest = len(removed) #removed best lengh
	lfit = []

	print('----> INITIAL BEST FITNESS IS: ' + str(best))

	for j in range(100):#in set
		print('######    THIS IS THE ' + str(j) + 'th ATTEMPT    ######')

		p = random.choice([0,1]) # one of two: add / delete

		if p:
			if B < len(edges):
				added = randomEdges(random.randrange(1,B+1),edges)
				isremoved = {e for e in added}
				recbest = fitness(graph, isremoved, infected)
				rrecbest = len(isremoved)

				if recbest < best: # less is better
					best = recbest
					removed = isremoved

				if  recbest == best: # equal

					if rrecbest < rbest: # less lengh
						removed = isremoved

					if rrecbest == rbest:
						pr = random.choice([0,1]) # random choice between removed
						if pr:
							removed = isremoved

		if not p:

			if len(removed)>0:
				lremoved = random.sample(removed, random.randint(1,len(removed))) # choose some from already removed
				recbest = fitness(graph, lremoved, infected)
				rrecbest = len(lremoved)

				if recbest <= best:
					best = recbest
					removed = lremoved
                    
		print('----> CURRENT BEST FITNESS IS: ' + str(best))
		lfit.append(best)

	plt.plot(range(len(lfit)),lfit)
