from collections import deque

def solution(n, edge):

    dist = [-1] * (n+1)
    graph = [[] for _ in range(n+1)]
    
    for data in edge:
        x, y = data[0], data[1]
        graph[x].append(y)
        graph[y].append(x)
    
    dist[1] = 0
    q = deque([1])
    while q:
        now = q.popleft()
        for i in graph[now]:
            if dist[i] == -1:
                dist[i] = dist[now] + 1
                q.append(i)
    
    max_value = max(dist)
    count = dist.count(max_value)
    
    return count
