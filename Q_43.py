import sys
sys.stdin = open("input.txt","r")

n, m = map(int,input().split())
array = []
result = 0
for i in range(m):
    data = list(map(int,input().split()))
    array.append(data)
    result += int(data[2])

array.sort(key = lambda x : x[2])

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

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i
    

temp = 0
for x,y,z in array:
    if find_parent(parent, x) != find_parent(parent,y) :
        union_parent(parent,x,y)
        temp += z


print(result - temp)
