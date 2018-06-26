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

isremoved = set()

#population
population = []
poprand = random.randint(5, 10) #minimalistic :D

for it in range(2*poprand): #size of population
	randEdge = randomEdges(random.randrange(1, B+1))
	removed = {i for i in randEdge}
	fit = fitness(graph, removed, infected)
	population.append((fit, removed))

#sampling
def sample(population):
	while population:
		x1 = random.randint(0,len(population))
		p1 = population[x1]
		population.remove(x1)

		x2 = random.randint(0,len(population))
		p2 = population[x2]
		population.remove(x2)

	return p1,p2

#cross
def cross(p1,p2,B, infected,graph):
	removed = set()

	for i in range(B):
		p = random.choice([0,1])
		if p:
			x1 = random.randint(0,len(p1[1]))
			removed.add(p1[1][x1])
			p1[1].remove(x1)

		else:
			x1 = random.randint(0,len(p2[1]))
			removed.add(p2[1][x1])
			p2[1].remove(x1)

    fit = fitness(graph, removed, infected)

	return fit, removed


#mutation
def mutate(child): #remove from child
	if 0.65 < random.random() < 1.0:
		child[1].pop()

	return child

child = []
i=0
while population:
	p1, p2 = sample(population)
	fit, removed = cross(p1, p2, B, infected, graph)
	child.append((fit, removed))
	child[i] = mutate(child[i])
	i += 1


 
