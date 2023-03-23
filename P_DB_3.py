from collections import deque

def solution(maps):
    
    n = len(maps)
    m = len(maps[0])
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    start = (0,0)
    q = deque([start])
    
    while q :
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y+ dy[i]
            
            if 0<=nx and nx< n and 0<=ny and ny<m :
                if maps[nx][ny] == 1:
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx,ny))
                    
    return maps[-1][-1] if maps[-1][-1] > 1 else -1