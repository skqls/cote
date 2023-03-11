import sys
sys.stdin = open("input.txt","r")
array = []
g = int(input())
p = int(input())
for i in range(p):
    array.append(int(input()))


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
    

parent = [0] * (g+1)
for i in range(g+1):
    parent[i] = i

count = 0

for i in array:
    a = find_parent(parent,i)
    if a != 0:
        union_parent(parent, a, a-1)
    else : 
        break
    count += 1

print(count)


