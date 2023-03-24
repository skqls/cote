import sys
sys.stdin = open("input.txt","r")

n = int(input())
array = list(map(int,input().split()))

def binary_search(array,s,e):
    if s > e:
        return None 
    
    mid = (s+e)//2
    
    if array[mid] == mid:
        return mid
    elif array[mid] < mid :
        return binary_search(array, mid+1, e)
    else:
        return binary_search(array, s, mid-1)


answer = binary_search(array, 0, n-1)
if answer == None :
    print(-1)
else : print(answer)