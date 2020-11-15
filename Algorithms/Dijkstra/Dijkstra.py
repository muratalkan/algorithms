import pandas as pd

def dijkstra(G, s, des):
    dists = {}
    preds = {}
    Q = {}

    if s not in G:
        raise TypeError("The root of the shortest path tree cannot be found!")
    if dest not in G:
        raise TypeError("The target of the shortest path cannot be found!")
    for v in G:
        dists[v] = float("inf")
        preds[v] = None
        Q[v] = float("inf")

    dists[s] = 0
    Q[s] = 0

    while Q:
        u = min(Q, key=Q.get)

        del Q[u]

        for neighbor in G[u]:
            if neighbor in Q:
                new_dists = dists[u] + G[u][neighbor]
                if new_dists < dists.get(neighbor):
                    dists[neighbor] = new_dists
                    Q[neighbor] = new_dists
                    preds[neighbor] = u
    return (dists, preds)

G = {}
v = []

n = int(input("Enter the number of vertices: "))
print("Enter the vertex list for the matrix: ")

for j in input():
    v.append(j)

MatrixDF = pd.read_excel("matrix.xlsx")

for i in range(n):
    key1 = v[i]
    dict2 = {}
    for j in range(n):
        key2 = v[j]
        if MatrixDF.iloc[i][j] !=0 :
            dict2[key2] = MatrixDF.iloc[i][j]
    G[key1] = dict2
    
print("\nGraph", G)

s = input("\nEnter the source: ")
dest = input("Enter the target: ")

dist,prev = dijkstra(G, s, dest)

path = []
pred = dest

while pred != None:
    path.append(pred)
    pred = prev.get(pred, None)

print("\nShortest Path-> " + str(path) + " Cost=" + str(dist[dest]))

