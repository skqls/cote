import sys
sys.stdin = open("input.txt","r")



n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a,b,c = map(int,input().split())
    if c < graph[a][b]:
        graph[a][b]= c


for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] != INF:
            print(graph[i][j], end=" ")
        else:
            print(0, end=" ")
    print()