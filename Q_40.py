import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline


import heapq

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

INF = int(1e9)
dist = [INF] * (n+1 )
dist[1] = 0

q = []
heapq.heappush(q,(0,1))

while q :
    cost, now = heapq.heappop(q)
    if cost < dist[now] :
        continue
    
    for i in graph[now]:
        if (cost + 1) < dist[i] :
            dist[i] = cost+1
            heapq.heappush(q,(cost+1,i))

max_value = -(1e9)
answer = 0
for i in range(1,n+1):
    if dist[i] > max_value:
        max_value = dist[i]
        max_node = i
        answer = 1
    elif dist[i] == max_value:
        answer +=1

print(max_node, max_value, answer)


