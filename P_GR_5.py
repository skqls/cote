def find_parent(parent, a ):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    
    if b < a:
        parent[a] = parent[b]
    else:
        parent[b] = parent[a]



def solution(n, costs):
    count = 0
    costs.sort(key= lambda x: x[2])
    parent = [0]*n
    for i in range(n):
        parent[i] = i
        
    for a,b,c in costs:
        if find_parent(parent,a) != find_parent(parent,b):
            count += c
            union_parent(parent,a,b)
    
    return count
    
         
    
    
    
    
    
    
    answer = 0
    return answer