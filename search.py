

from heapq import heappop , heappush

from math import radians, cos, sin, asin, sqrt

import Graph



class Search:

    def __init__(self):
        self.visited_nodes = []
        self.Adjecents = []
        self.total_node = []


    def distance(self,t1,t2):
        

        lon1 = radians(t1[1])
        lon2 = radians(t2[1])
        lat1 = radians(t1[0])
        lat2 = radians(t2[0])
        
        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    
        c = 2 * asin(sqrt(a))
        r = 6371

        return(c * r)

    def getlow(self,dic,adj):
        con = []
        val = 0
        save = 0
        if len(adj) > 0:
            for c in adj:
                con.append(dic[c])


            min = con[0]
            save = 0
            for i in range(0,len(adj),1):
                if adj[i] < min:
                    min = adj[i]
                    save = i
        val = adj[save]
        min = dic[val]
        adj.pop(save)
        
        return val,min

    
   
         
    def BFS_two(self,g,intial_node,final_node):
       # recursive Implementation of BFS 
        path = []
        visited_nodes = []
        self.visited_nodes.append(intial_node)
        adj_List = g.getAdjecents(intial_node)
        for i in adj_List:
            if i not in self.visited_nodes and i not in self.Adjecents:
                self.Adjecents.append(i)

        if final_node not in self.visited_nodes:
            intial_node = self.Adjecents.pop(0)
            self.BFS_two(g,intial_node,final_node)
        
        else:
            
            x = []
            x += self.visited_nodes
            isTrue = True  
            while len(x) != 0:
                poped = x.pop(-1)
                path.append(poped)
                adj = g.getAdjecents(poped)
                if len(x) > 0:
                    for i in range(len(x)):
                        if x[i] in adj:
                            x = x[:i+1]
                            break

            for i in range(len(path)//2):
                path[i],path[-i-1] = path[-i-1],path[i]
                
            print(path)
        
            
        return self.visited_nodes

    
    def DFS_two(self,g,intial_node,final_node):

        #recursive implementation of DFS
        path = []
        self.visited_nodes.append(intial_node)
        adjs = g.getAdjecents(intial_node)
        for i in adjs:
            if i not in self.visited_nodes and i not in self.Adjecents:
                self.Adjecents.append(i)

        if final_node not in self.visited_nodes:
            intial_node = self.Adjecents.pop(-1)
            self.DFS_two(g,intial_node,final_node)

        else:
            x = []
            
            x += self.visited_nodes
            isTrue = True  
            while len(x) != 0:
                poped = x.pop(-1)
                path.append(poped)
                adj = g.getAdjecents(poped)
                if len(x) > 0:
                    for i in range(len(x)):
                        if x[i] in adj:
                            x = x[:i+1]
                            break
        # print(path)
        
        return self.visited_nodes
   
  
    def DFS(self,g,node_name,target):

          #iterative implemenation of DFS
        visited_nodes = []
        visited_nodes.append(node_name)

        while target not in visited_nodes:
            adj = g.getAdjecents(node_name)
            for i in adj:
                if i not in visited_nodes and i not in self.Adjecents: 
                    self.Adjecents.append(i)
            
            node_name = self.Adjecents.pop(-1)
            visited_nodes.append(node_name)
        return visited_nodes

  
    
    def Dijkstra(self,g,node_name,target):

        dic = {}
        visited = []     # holdes  node_names which are visited
        dic[node_name] = 0   #intializing the first dictionary element
        container = []        # hold consecutive adjcents of the preceeding node_name
        cost = 0
        for i in g.edges.keys():
            if i not in dic:
                dic[i] = float('inf')

        # container.append(node_name)  
        heappush(container,(0,node_name))
        while container:
            
            
            current = heappop(container)
            
            visited.append(current[1])
            for j in g.getAdjecents(current[1]):

                cost = (g.getWeight(current[1],j) + current[0])
                if j == target:
                    
                    if cost < dic[j]:
                        dic[j] = g.getWeight(current[1],j) + current[0]
                    # container.append(j)
                    heappush(container,(cost,j))
                    self.visited_nodes.append(i)
                    break


                if j not in visited:
                    
                    cost = (g.getWeight(current[1],j) + current[0])
                    if cost < dic[j]:
                        dic[j] = g.getWeight(current[1],j) + current[0]
                    
                    # container.append(j)
                    heappush(container,(cost,j))
                   
            
                
        return dic
     

     

    def A_star(self,g,node_name,target):
        path = {}
        short_path = 0
        opened = []  # this list collects the vertices whose adjcents are to be accessed
        closed = []  # this list collects the vertices whose adjcents are  accessed
        dic = {}   # this dictionary holds the key(node name) and values((weight ,heurstic value))
        hursitc = {} # used to assist the dic dictionary by leaving the weight just the heuristic value and key
        cost = 0 # intial weight for the starting node
        isStarted = True

        
        for i in g.edges.keys():
            if i != node_name:
                dic[i] = [float('inf'),self.distance(g.locaton[i],g.locaton[target])]
            else:
                dic[i] = [0,self.distance(g.locaton[i],g.locaton[target])]
       
        heappush(opened,(0,node_name))
        self.visited_nodes.append(node_name)
        while opened and isStarted:

            current = heappop(opened)
            if current[1] not in closed:
                closed.append(current[1])
            for i in g.getAdjecents(current[1]):# getAdjecents bring adjecents of the node name given
                
                if i == target:
                    cost = (g.getWeight(i,current[1]) + current[0]) 
                    if cost < (dic[i][0]):
                        dic[i][0] = cost
                        dic[i][1] = dic[i][1] + cost
                        path[i] = current[1]
                        
                    j = 0
                    if i not in closed:
                        closed.append(i)
                    for i in dic.keys():
                        
                        hursitc[i] = dic[i][0]
                   #huristic[target]
                    return hursitc
                

                if i in closed:
                    continue
                cost = (g.getWeight(i,current[1]) + current[0]) 
                if cost < (dic[i][0]):
                    dic[i][0] = g.getWeight(i,current[1]) + current[0]
                    dic[i][1] = g.getWeight(i,current[1]) + current[0] + dic[i][1]
                    path[i] = current[1]
                heappush(opened,(dic[i][0],i))
                if i not in self.visited_nodes:
                    self.visited_nodes.append(i)
                
               
        
