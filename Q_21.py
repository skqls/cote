# 6 5
# 1 1 0 1 1
# 0 1 1 0 0
# 0 0 0 0 0
# 1 0 1 1 1
# 0 0 1 1 1
# 0 0 1 1 1

import sys
sys.stdin = open("input.txt","r")

from collections import deque 
n, m = map(int,input().split())

graph = []

for i in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,1,0,0]

dy =  [0,0,-1,1]
check = [[False] * m for _ in range(n)]


def bfs(x,y):
    q = deque([(x,y)])
    width = 0
    while q : 
        x,y = q.popleft()
        graph[x][y]= 0
        check[x][y]=True
        width += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx and nx<n and 0<= ny and ny < m :
                if graph[nx][ny] == 1 and check[nx][ny]== False :
                    q.append((nx,ny))
    return width



answer = int(-1e9)
count = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            width = bfs(i,j)
            count += 1
            answer = max(answer, width)

print(count)
print(answer)


