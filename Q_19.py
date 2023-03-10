import sys
sys.stdin = open("input.txt","r")

n = int(input())
array = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())
max_value = -int(1e9)
min_value = int(1e9)


def dfs(count, value):
    global min_value, max_value, add, sub, mul, div
    
    if count == n:
        min_value = min(min_value, value)
        max_value = max(max_value, value)
        return
    
    if add > 0 :
        add -= 1
        dfs(count+1,value+array[count])
        add += 1
    
    if sub > 0 :
        sub -= 1
        dfs(count+1,value-array[count])
        sub += 1

    if mul > 0 :
        mul -= 1
        dfs(count+1,value*array[count])
        mul += 1

    if div > 0 :
        div -= 1
        dfs(count+1,int(value/array[count]))
        div += 1

dfs(1,array[0])
print(max_value)
print(min_value)




