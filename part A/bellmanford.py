#belman ford
from sys import maxsize
class graph:
    def __init__ (self,vert):
        self.V=vert
        self.graph=[]
    
    def add_edge(self,src,dest,w):
        self.graph.append([src,dest,w])
        
    def printdist(self,dist):
        print("Vertex\t\tDistance from source")
        for i in range (len(dist)):
            dist[i] = -1 if dist[i]==maxsize else dist[i]
            print(f'{i}\t\t{dist[i]}')
    
    def belmann(self,src):
        dist=[maxsize]*self.V
        dist[src]=0
        for i in range (self.V-1):
            for u,v,w in self.graph:
                if dist[u]!=maxsize and dist[u]+w<dist[v]:
                    dist[v]=dist[u]+w
        
        for u,v,w in self.graph:
                if dist[u]!=maxsize and dist[u]+w<dist[v]:
                    print("Negative Cycle")
                    return
        self.printdist(dist)

vert=int(input("Enter numb of vertices"))
edg=int(input("Enter numb of edges"))
g=graph(vert)
for _ in range (edg):
    src=int(input("Source: "))
    dest=int(input("Dest: "))
    w=int(input("Weight: "))
    g.add_edge(src,dest,w)

source=int(input("Input source: "))
g.belmann(source)
                    
