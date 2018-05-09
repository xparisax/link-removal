import random

graph = {
	1: {2,6},
	2: {1,3},
	3: {2, 4, 6},
	4: {3,5},
	5: {4,6},
	6: {3,1,5}
}

infected = {2,5}
removed = set()

def random_edge(graph, removed):
	edges = [(u, v)
		for u, vs in graph.items()
		for v in vs
		if u< v if (u,v) not in removed
	]
	return random.choice(edges)

def get_susceptibles(graph, infected, removed):
	susceptible = set()

	def dfs(node):
		if node in susceptible:
			return

		susceptible.add(node)
		for dst in graph[node]:
			if (node, dst) in removed:
				continue

			if (dst, node) in removed:
				continue

			dfs(dst)

	for v in infected:
		dfs(v)

	return (susceptible - infected)

for i in range(4):
	removed.add(random_edge(graph, removed))

min_ = len(get_susceptibles(graph, infected, removed))

for k in range(100):
	e = random.choice(list(removed))
	removed.remove(e)
	n = random_edge(graph, removed)
	removed.add(n)

	fitness = len(get_susceptibles(graph, infected, removed))
	if (fitness > min_ or random.random() < p):
		removed.remove(n)
		removed.add(e)
	else:
		min_ = fitness

	print(k , removed, fitness, min_)
