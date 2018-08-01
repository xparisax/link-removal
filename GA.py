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


def randomEdges(n, edges): #added some check for sampling problem: negetive or positive range
	if n <= len(edges):
		e = random.sample(edges, n)
	else:
		while n > len(edges):
			n -= 1
		e = random.sample(edges, n)

	return e #list


def susCounter(graph, infected):
	inf = list(infected)
	susReturn = 0

	for i in xrange(0, len(inf)):
		susReturn += len(graph[inf[i]])
		for j in xrange(0, len(graph[inf[i]])):
			checker = graph[inf[i]][j]
			susReturn += len(graph[checker])

	return susReturn #number


def fitness(graph, removed, infected): # handeling single and multiple edges removed
	inpGraph = list(graph.values())
	inpRemoved = list(removed)

	if len(removed) == 1: #[(1,2)]
		u , v = removed
		inpGraph[u].pop(inpGraph[u].index(v))
		inpGraph[v].pop(inpGraph[v].index(u))

		sus = susCounter(inpGraph, infected)

		inpGraph[u].append(v)
		inpGraph[v].append(u)

	else:
		for x in inpRemoved:#[(1,2),(2,3),...]
			u , v = x
			inpGraph[u].pop(inpGraph[u].index(v))
			inpGraph[v].pop(inpGraph[v].index(u))
		
		sus = susCounter(inpGraph, infected)

		for x in inpRemoved:
			u, v = x
			inpGraph[u].append(v)
			inpGraph[v].append(u)
	
	return sus #number


def population(n, B, edges):
	popList = []

	for i in range(n):
		popList.append(randomEdges(B, edges)) # population of removed's'

	return popList #[[edges],[]]


def cross(p1, p2):
    crossLen = random.choice(range(len(p1[0]))) # random cross point
    if crossLen == 0:
		crossLen += 1
    
    t = randomEdges(crossLen, p1[0])
    s = randomEdges(len(p1[0])-crossLen, p2[0])

    for i in range(len(s)):
        if s[i] not in t :
            t.append(s[i])
        
    while len(p1) > len(t) :
        ch = randomEdges(1, p1[0])
        while ch in t :
            ch = randomEdges(1, p1[0])
        t.append(ch)

    return t


def mutate(child, i, edges):
	muteCandidate = random.choice(range(len(child))) #candidate to mutate
	muteProb = random.random() # mutate probability

	if muteProb < (1/(i+10)): #draw
		child.pop(muteCandidate) #drops the child
        mutated = randomEdges(1, edges)

        while mutated[0] in child:
            mutated = randomEdges(1, edges)    
		
        child.extend(mutated) #adds instead

	return child


def fitList(population): # list of fitness of population and sorting
	fitValues = []
	fitPop = []

	for i in range(len(population)):
		fit = fitness(graph, population[i], infected)
		fitValues.append(fit)
		fitPop.append(population[i])

		for j in range(len(fitValues)):
			if fit > fitValues[len(fitValues)-j-1]:
				temp = fitValues[len(fitValues)-j-1]
				temp1 = fitPop[len(fitPop)-j-1]

				fitValues[len(fitValues)-j-1] = fit
				fitPop[len(fitPop)-j-1] = population[i]

				fit = temp
				population[i] = temp1

	return fitPop, fitValues


def generation(child, population, popNum):
    childFit = fitness(graph, child, infected)
    pplList , value = fitList(population)

    if len(pplList) < popNum:
        pplList.append(child)

    elif childFit > value[len(value)-1]: #else if list equal num -and- was a better child
        if len(population)>1:
            population.pop(len(pplList)-1)
            population.append(child)
            pplList = population

    return pplList


ppl = population(100, B, edges)
ppls = []
for i in range(100):
    p1 = random.sample(ppl,1)#[[(edges)]]
    p2 = random.sample(ppl,1) 
    child = cross(p1,p2)
    mutateChild = mutate(child, i, edges)
    ppls = generation(mutateChild, ppl, len(ppl))
    ppl = ppls

pplList , value = fitList(ppl)
print(pplList[0], value[0])


    # while p2==p1:
    #     p2 = random.sample(ppl,1) 
