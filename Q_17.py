from collections import deque

n,k = map(int,input().split())
graph = []
data = []

for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] != 0:
            data.append((0, graph[i][j], i,j))

data.sort(key = lambda x: x[1])

q = deque(data)

target_s, target_x, target_y = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]


while q :
    time, virus, x,y = q.popleft()
    if time == target_s :

        break
    else :
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx and nx <n and 0<=ny and ny<n:
                if graph[nx][ny]==0:
                    graph[nx][ny]=virus
                    q.append((time+1,virus,nx,ny))

print(graph[target_x-1][target_y-1])





