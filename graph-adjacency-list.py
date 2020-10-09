# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 11:04:21 2020

@author: kamyar

Implementation of a undirected, unweighted graph using adjacency list
"""

class Graph():
    def __init__(self):
        self.totalnodes = 0
        self.adjacency_list = {}
        
    def AddVertex(self,node):   
        self.adjacency_list[node] = []            
        self.totalnodes += 1
    
    def AddEdge(self, node1, node2):
        if self.totalnodes == 0:
            print("please add Nodes first before defining edges and try again.")
            pass
        else:
            if (node1 in self.adjacency_list.keys()) and (node2 in self.adjacency_list.keys()):
                self.adjacency_list[node1].append(node2)
                self.adjacency_list[node2].append(node1)
            else:
                print('invalid nodes!\nPlease make sure that the desired nodes are defined in the graph before creating edges for them')
    
    def PrintGraph(self):
        for i in self.adjacency_list.keys():
            print('{} --> {}'.format(i, self.adjacency_list[i]))
    
G = Graph()
G.AddVertex(0)
G.AddVertex(1)
G.AddVertex(2)
G.AddVertex(3)
G.AddVertex(4)
G.AddVertex(5)
G.AddVertex(6)
G.AddEdge(3,1)
G.AddEdge(3,4)
G.AddEdge(4,2)
G.AddEdge(4,5)
G.AddEdge(1,2)
G.AddEdge(1,0)
G.AddEdge(0,2)
G.AddEdge(6,5)
G.PrintGraph()
    