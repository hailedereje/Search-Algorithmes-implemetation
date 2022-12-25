import search
import Graph

g = Graph.Graph()
data = Graph.DataReader()
data.file_reader(g,"sample.txt")
data.location_reader(g,"other")

Search = search.Search()
# for i in g.vertices:
# print(Search.Dijkstra(g,"Neamt","Arad")["Arad"])
print(Search.DFS_two(g,"Zerind","Sibiu"))
