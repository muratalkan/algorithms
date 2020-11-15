def BfsRec(graph, node):
   visited = []
   queue = []
   visited.append(node)
   queue.append(node)

   while queue:
       s = queue.pop(0)
       for neighbor in graph[s]:
           if neighbor not in visited:
               visited.append(neighbor)
               queue.append(neighbor)
   return visited

Graph = {}
matrix = []
vertex = []

n = int(input("Enter the number of vertices: "))

print("Enter the vertext list for graph: ")
for i in input():
    vertex.append(i)

print("Enter the adjacency matrix: ")
for k in range(n):
    matrix.append([int(j) for j in input().split()])

for i in range(n):
    List = []
    for j in range(n):
        if matrix[i][j] == 1:
            List.append(vertex[j])
        key = vertex[i]
        Graph[key]=List

print("The graph is")
print(Graph)
print("BFS Traversal:")
print(BfsRec(Graph, 'a'))
