n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2
adjList = {}

adjacencyList = {_} for _ in range(n)
print(adjacencyList)
for (origin, dest) in edges:
    adjacencyList[origin].append(dest)
print(adjacencyList)

for element in range(len(adjacencyList[origin])):
    if element == source and destination in adjacencyList[element]:
                # if element == destination or source in self.adjacencyList[element]:
        print(True)
    else:
        print(False)
