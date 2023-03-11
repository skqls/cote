from collections import deque

for tc in int(input()):
    n = int(input())
    ranking = list(map(int, input().split()))
    m = int(input())
    changes = []
    for i in range(n):
        changes.append(list(map(int,input().split())))
    

    indegree = [0]*(n)
    graph= [[False]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            indegree[ranking[j]]+=1
            graph[j][i]= True

    

    for change in changes:
        i,j = change[0], change[1]
        if graph[j][i]:
            indegree[j]+=1
            indegree[i]-=1
            graph[j][i]=False
            graph[i][j]=True
        
        else :
            indegree[i]+=1
            indegree[j]-=1
            graph[i][j]=False
            graph[j][i]=True

    q = deque()

    for i in len(indegree):
        if indegree[i] == 0:
            q.append(i)

    abstract = False
    consistent = True
    
    while True:
        if len(q) == 0:
            abstract = True 
            break
        if len(q) >= 2:
            consistent = False
            break
        now = q.popleft()
        for a in range(n):
            if graph[]







