from heapq import heappop , heappush
import time
from math import radians, cos, sin, asin, sqrt

class Node:

    def __init__(self,name):
        self.name = name
        self.nodes_connected = []

           
class Graph:

   
    def __init__(self): 
        self.edges = {}
        self.vertices = []
        self.nodes = []
        self.visited_nodes = []
        self.Adjecents = []
        self.locaton = {}
        
        

    def create_node(self,node_name):
       
        if node_name not in self.vertices:
            node = Node(node_name)
            self.vertices.append(node.name)
            self.nodes.append(node)
            return node
        else:
            for i in range(len(self.vertices)):
                if self.vertices[i] == node_name:
                    return self.nodes[i]

    def create_edge(self,node1,node2,weight):
        
        node1.nodes_connected.append((node2.name,weight))
        node2.nodes_connected.append((node1.name,weight))
        self.edges[node1.name] = node1.nodes_connected
        self.edges[node2.name] = node2.nodes_connected
       

    def isEdge(self,node1,node2):
        for i in self.edges[node1.name]:
            
            if i[0] == node2.name:
                return True
            else:
                return False
    
    def numOfNodesConnected(self,node):
        numOfNode = len(self.edges[node.name])
        return numOfNode

    def getNode(self,node_name):

        for i in range(len(self.vertices)):
                if self.vertices[i] == node_name:
                    return self.nodes[i]
                
    def getAdjecents(self,node_name):
        node = self.getNode(node_name)
        x = []
        if node != None:
            if len(node.nodes_connected) > 0:
                for i in range(len(node.nodes_connected)):
                    x.append(node.nodes_connected[i][0])
        return x

    def getWeight(self,node1_name,node2_name):
        x = self.edges[node1_name]
        for i in x :
            if i[0] == node2_name:
                return i[1]
            

class DataReader:
    def __init__(self):
        pass

    def file_reader(self,g,file_name):

        file = open(file_name, "r")
        lines = file.readlines()

        for line in lines:
            l = line.split()
            n = g.create_node(l[0])
            n2 = g.create_node(l[1])
            g.create_edge(n,n2,float(l[2]))
    def location_reader(self,g,file_name):
        file = open(file_name,"r")
        lines = file.readlines()
        for line in lines:
            l = line.split()
            g.locaton[l[0]] = (float(l[1]),float(l[2]))
























        






