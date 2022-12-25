import search
import Graph
import time
import timeit

g = Graph.Graph()
data = Graph.DataReader()
data.file_reader(g,"sample.txt")
data.location_reader(g,"other")

Search = search.Search()
count = 0

sum = 0
path = 0
for a in g.vertices:
    for b in g.vertices:
    
        start = time.time()
        path = len(Search.Dijkstra(g,a,b))
        # Search.BFS_two(g,a,b)
        # Search.DFS_two(g,a,b)
        # Search.A_star(g,a,b)
        # result = timeit.timeit('Search.DFS(g,a,b)', globals=globals(), number=10000)
        end = time.time()
        sum += end - start
        g.visited_nodes = []


# print(sum / 400,len(path))
print(path/380)

