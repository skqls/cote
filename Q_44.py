import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

n = int(input())


x = []
y = []
z = []

for i in range(n):
    data = list(map(int,input().split()))
    x.append((data[0],i))
    y.append((data[1],i))
    z.append((data[2],i))

x.sort()
y.sort()
z.sort()

edges = []

for i in range(n-1):
    edges.append([x[i+1][0]-x[i][0],x[i][1],x[i+1][1]])
    edges.append([y[i+1][0]-y[i][0],y[i][1],y[i+1][1]])
    edges.append([z[i+1][0]-z[i][0],z[i][1],z[i+1][1]])

edges.sort()



def find_parent(parent,a):
    if parent[a] != a:
        parent[a] = find_parent(parent,parent[a])
    return parent[a]

    

def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b )

    if a< b :
        parent[b] = parent[a]
    else : 
        parent[a] = parent[b]

parent = [0] * (n)
for i in range(n):
    parent[i] = i

result = 0

for edge in edges :
    if find_parent(parent, edge[1]) != find_parent(parent,edge[2]):
        union_parent(parent,edge[1],edge[2])
        result += edge[0]

print(result)





