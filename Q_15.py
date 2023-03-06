from collections import deque
from sys import stdin
input = stdin.readline
n, m, k, x = map(int, input().split())

INF = 1e9
dist = [INF] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque([(x, 0)])   
dist[x] = 0
while q:
    now, d = q.popleft()
    for i in graph[now]:
        if dist[i] == INF:
            dist[i] = d + 1
            q.append((i, d + 1))   

check = False
for i in range(1, n + 1):
    if dist[i] == k:
        print(i)
        check = True

if not check:
    print(-1)