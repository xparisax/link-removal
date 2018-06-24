from graphInput import * 

myFile = open('input.txt', 'r')

def randomEdges(n):
	edge = []
	edges = []

	for line in myFile:
		edge.append(line)
		edge = [x.strip() for x in edge]

	for i in range(len(edge)):
		u, v = edge[i].split()
		edges.append((int(u),int(v)))

	return random.sample(edges, n)


def fitness(gragh, removed, infected):
	susceptible = set()

	def dfs(node):
		if node in susceptible:
			return

		susceptible.add(node)
		for u in graph[node]:
			if (node, u) in removed:
				continue

			if (u, node) in removed:
				continue

			dfs(u)

	for v in infected:
		dfs(v)

	return len(susceptible - infected)

for i in range(100):
	print('############    THIS IS THE ' + str(i) + 'th ATTEMPT    ############')

	randEdge = randomEdges(random.randrange(1,B+1))
	removed = {i for i in randEdge}
	best = fitness(graph, removed, infected)
	rbest = len(removed)
	#print('REMOVED EDGES ARE: ' + removed + '\n' +
	#	'BEST FITNESS IS: ' + best + '\n')

	while len(removed) <= B:

		p = random.choice([0,1])

		if p:
			added = randomEdges(random.randrange(1,B+1))
			isremoved = {e for e in added}

			recbest = fitness(graph, isremoved, infected)
			rrecbest = len(isremoved)

			if recbest < best:
				best = recbest
				removed = isremoved

			if  recbest == best:

				if rrecbest < rbest:
					removed = isremoved

				if rrecbest == rbest:
					pr = random.choice([0,1])
					if pr:
						removed = isremoved

		if not p:

			lremoved = random.sample(removed, random.randint(1, rbest-1))
			recbest = fitness(graph, lremoved, infected)
			rrecbest = len(lremoved)

			if recbest <= best:
				best = recbest
				removed = isremoved


		#print('REMOVED EDGES ARE: ' + removed + '\n' +
		#'BEST FITNESS IS: ' + str(best) + '\n')
