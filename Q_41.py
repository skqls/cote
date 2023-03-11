import sys
sys.stdin = open("input.txt","r")

n, m = map(int,input().split())

def find_parent(parent,i):
    if parent[i] != i :
        parent[i] = find_parent(parent,parent[i])
    return parent[i]


def union_parent(parent, a, b):
    a= find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b :
        parent[b] = parent[a]
    else :
        parent[a] = parent[b]


parent = [0]*(n+1)

for i in range(1,n+1):
    parent[i] = i

graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        if graph[i][j] == 1 :
            union_parent(parent, i , j)

check = True

data = list(map(int,input().split()))
for i in range(len(data)-1) :
    if parent[i] != parent[i+1]:
        check = False

if check:
    print("YES")
else : print("NO")