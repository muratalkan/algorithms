from collections import defaultdict 

class Graph: 
    def __init__(self, verts): 
        self.graph = defaultdict(list)
        self.V = verts
  
    def addEdge(self, u, v): 
        self.graph[u].append(v) 
  
    def topologicalSortUtil(self, v, visit, stack):  
        visit[v] = True
  
        for i in self.graph[v]: 
            if visit[i] == False: 
                self.topologicalSortUtil(i, visit, stack) 
  
        stack.insert(0, v) 

    def topologicalSort(self): 
        visit = [False] * self.V 
        stack = [] 

        for i in range(self.V): 
            if visit[i] == False: 
                self.topologicalSortUtil(i, visit, stack) 

        print(stack) 
  
gr = Graph(6) 
gr.addEdge(5, 2); 
gr.addEdge(5, 0); 
gr.addEdge(4, 0); 
gr.addEdge(4, 1); 
gr.addEdge(2, 3); 
gr.addEdge(3, 1); 
  
print("Topological Sort of the given graph")
gr.topologicalSort() 
