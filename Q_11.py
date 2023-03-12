import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

from collections import deque

n = int(input())
k = int(input())

graph = [[-1] * (n+2) for _ in range(n+2)]
for i in range(n):
    for j in range(n):
        graph[1+i][1+j] = 0

for i in range(k):
    x,y = list(map(int,input().split()))
    graph[x][y] = 2

dx = [-1,0,1,0]
dy = [0,-1,0,1]

changes = []
l = int(input())
for i in range(l):
    data = input().split()
    changes.append([int(data[0]),data[1]])


def turn(plan,direction):
    if plan == "D" :
        direction = (direction-1)%4
    else :
        direction = (direction+1)%4
    return direction

        

x,y = 1,1
count = 0
q = deque([(x,y)])
graph[x][y]=1
direction = 3
dir = 0
while True:
    nx = x+ dx[direction]
    ny = y+ dy[direction]
    if 1<=nx and nx<=n and 1<=ny and ny<= n and graph[nx][ny] !=-1 and graph[nx][ny] != 1:
        
        if graph[nx][ny] == 2:
            graph[nx][ny] = 1
            q.append((nx,ny))
        
        else :
            graph[nx][ny] = 1
            a,b = q.popleft()
            graph[a][b]=0
            q.append((nx,ny))

        count +=1
        x,y = nx,ny
        if dir < l and changes[dir][0] == count :
            direction = turn(changes[dir][1],direction)
            dir += 1

            



    else:
        count +=1
        break

print(count)




        




