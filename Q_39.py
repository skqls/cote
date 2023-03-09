import sys
import heapq
sys.stdin = open("input.txt","r")


for tc in range(int(input())):

    n = int(input())

    dx=[-1,1,0,0]
    dy=[0,0,-1,1]

    INF = int(1e9)
    graph = []
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        graph.append(list(map(int,input().split())))

    x,y = 0,0
    q = []
    dist[x][y] = graph[x][y]
    heapq.heappush(q,(graph[x][y],x,y))

    while q:
        value , x, y = heapq.heappop(q)
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx and nx<n and 0<=ny and ny<n :
                cost = value + graph[nx][ny]
                if cost < dist[nx][ny]:
                    heapq.heappush(q,(cost,nx,ny))
                    dist[nx][ny] = cost

    print(dist[n-1][n-1])






    



        
