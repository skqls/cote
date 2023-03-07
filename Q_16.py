from sys import stdin
input = stdin.readline
n,m = map(int,input().split())
temp = [[0]*m for _ in range(n)]
result = 0
array = []
for i in range(n):
    array.append(list(map(int,input().split())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]


def virus(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx and nx<n and 0<=ny and ny<m:
            if temp[nx][ny] == 0:
                temp[nx][ny] =2 
                virus(nx,ny)

                
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score +=1
    return score





def solution(count):
    global result
    if count == 3:
        
        for i in range(n):
            for j in range(m):
                temp[i][j]= array[i][j]
        
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
        
        result = max(result, get_score())
        return

    

    else :
        for i in range(n):
            for j in range(m):
                if array[i][j]==0:
                    array[i][j]=1
                    count += 1
                    solution(count)
                    array[i][j]=0
                    count -= 1

solution(0)
print(result)