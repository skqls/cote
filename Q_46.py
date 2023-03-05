# 46

from collections import deque

INF = 1e9

now_x,now_y = 0,0
now_size = 2
n = int(input())
array = []
for i in range(n):
    array.append(list(map(int,input().split())))


for i in range(n) :
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i,j
            array[now_x][now_y]=0

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    x,y = now_x, now_y
    dist = [[-1]*n for _ in range(n)]
    dist[x][y] = 0
    q = deque([(x,y)])
    while q : 
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx and nx<n and 0<=ny and ny<n :
                if array[nx][ny] <=now_size and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y]+1
                    q.append((nx,ny))
    return dist

def find(dist):
    min_dist = INF
    x,y = 0,0
    for i in range(n):
        for j in range(n):
            if dist[i][j]!= -1 and 1<= array[i][j] and array[i][j]<now_size:
                if dist[i][j] < min_dist:
                    min_dist = dist[i][j]
                    x,y = i,j
    
    if min_dist == INF :
        return None
    else:
        return (x,y,min_dist)

result = 0
ate = 0

while True:
    value = find(bfs())
    if value == None:
        print(result)
        break
    else:
        now_x,now_y = value[0],value[1]
        result += value[2]
        array[now_x][now_y] = 0
        ate += 1

        if ate >= now_size:
            now_size+=1
            ate = 0

        