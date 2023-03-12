import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

from collections import deque

for tc in range(int(input())):
    n = int(input())
    ranking = list(map(int, input().split()))
    m = int(input())
    changes = []
    for i in range(m):
        changes.append(list(map(int,input().split())))
    

    indegree = [0]*(n+1)
    graph= [[False]*(n+1) for _ in range(n+1)]



    for i in range(n):
        for j in range(i+1,n):
            indegree[ranking[j]]+=1
            graph[ranking[i]][ranking[j]]=True
    

    for change in changes:
        i,j = change[0], change[1]
        if graph[i][j]:
            indegree[i]+=1
            indegree[j]-=1
            graph[i][j]=False
            graph[j][i]=True

        else:
            indegree[j]+=1
            indegree[i]-=1
            graph[j][i]=False
            graph[i][j]=True

    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    abstract = False
    consistent = True
    answer = []

    for i in range(n):
        if len(q) == 0:
            abstract = True 
            break
        if len(q) >= 2:
            consistent = False
            break
        now = q.popleft()
        answer.append(now)
        for i in range(1,n+1):
            if graph[now][i]:
                indegree[i]-=1
                if indegree[i] == 0:
                    q.append(i)
    
    if abstract == True:
        print("IMPOSSIBLE")
    elif consistent == False:
        print("?")
    else:
        print(answer)











