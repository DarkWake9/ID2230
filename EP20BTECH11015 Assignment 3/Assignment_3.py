#Program to store the gievn file in an adjacency list manner
#and prompt the user to input any two nodes and
# return the shortest path and distance between the two nodes

import numpy as np
import pandas as pd


#Graph in adjacency list form
class Graph:
    
    def __init__(self, noof_vertices):
        self.noof_vertices = noof_vertices
        self.adjlist = [[] for v in range(self.noof_vertices)]*self.noof_vertices

    #Function to connect two nodes in an UNDIRECTED graph    
    def connect(self, node1, node2):
        temp1 = self.adjlist[node1]
        temp2 = self.adjlist[node2]
        if node2 not in self.adjlist[node1]:
            temp1.append(node2)
            self.adjlist[node1] = temp1
        
        temp2 = self.adjlist[node2]
        if node1 not in self.adjlist[node2]:
            temp2.append(node1)
            self.adjlist[node2] = temp2            

    #Function to return the shortest path between two nodes
    #  in a given adjacency list via modified BFS algo
    def bfs(self, node1, node2):
        visited = [False]*len(self.adjlist)
        queue = [[node1]]
        distance = 0
        while queue:
            
            path = queue.pop(0)
            node = path[-1]
            distance = len(path)    #Distance between two nodes is the number edges in the SHORTEST path between the two nodes

            if node == node2:
                return (path,distance - 1)

            if visited[node] == False:
                visited[node] = True
                nextlvl = self.adjlist[node]

                for tempnode in nextlvl:
                    if visited[tempnode] == True:
                        continue
                    else:
                        temp = list(path)
                        temp.append(tempnode)
                        queue.append(temp)            
        else:
            return ["The two nodes are not connected", '-1']
#Driving function
def drive():
    #Importing data from the file and storing it as an adjacency list
    data = np.array(pd.read_csv("fb-pages-sport.csv"))
    noof_edges = len(data)
    noof_vertices = max(data[i][0] for i in range(0, noof_edges))
    
    graph = Graph(noof_vertices)
    for i in range(0, noof_edges): #Loop to store the data as adjacency list
        graph.connect(data[i][0], data[i][1])

    #Taking the input from the user:
    node1 = int(input("Enter the index of node 1: "))
    node2 = int(input("Enter the index of node 2: "))

    #Validating and processing the input
    if node1 > noof_vertices or node2 > noof_vertices or node1 < 0 or node2 < 0:
        print("Invalid node")
    elif node1 == node2:
         print("Same node")
    else:
        path, distance =(graph.bfs(node1,node2))
        print(f"Path: {path},   Distance: {distance}")

drive()