def DfsRec(Graph, vert, path=[]):
    path += [vert]

    for neighbor in Graph[vert]:
        if neighbor not in path:
            path = DfsRec(Graph, neighbor, path)

    return path

Graph = {}
matrix = []
vert = []

n = int(input("Enter the number of vertices: "))

print("Enter the vertex list for graph: ")
for i in input():
    vert.append(i)

print("Enter the adjacency matrix: ")
for k in range(n):
    matrix.append([int(j) for j in input().split()])

for i in range(n):
    List = []
    for j in range(n):
        if matrix[i][j] == 1:
            List.append(vert[j])
        key = vert[i]
        Graph[key] = List

print("\nThe graph is")
print(Graph)
print("\nDFS Traversal:")
print(DfsRec(Graph, 'a'))
