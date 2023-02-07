#bellman ford
from sys import maxsize
class graph:
    def __init__ (self,vert):
        self.V=vert
        self.graph=[]
        
    def add_edge(self,src,dest,weight):
        self.graph.append([src,dest,weight])
        
    def print_dist(self,dist):
        print("Vertex\t\tDistance from source\n")
        for i in range (self.V):
            print(f'{i}\t\t{dist[i]}')
    
    def bellman(self,src):
        dist=[maxsize]*self.V
        dist[src]=0
        for i in range (self.V - 1):
            for u,v,w in self.graph:
                if dist[u]!=maxsize and dist[u]+w<dist[v]:
                    dist[v]=dist[u]+w
                    
        for u,v,w in self.graph:
            if dist[u]!=maxsize and dist[u]+w<dist[v]:
                print("Graph has negative cycle")
                return
            
        self.print_dist(dist)
        
num=int(input("Enter number of vertices in the graph"))
edg=int(input("Enter number of edges in the graph"))
g=graph(num)
for _ in range (edg):
    src=int(input("Enter source:"))
    dest=int(input("Enter destination:"))
    w=int(input("Enter weight:"))
    g.add_edge(src,dest,w)

g.bellman(0)
