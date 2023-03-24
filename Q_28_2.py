import sys
sys.stdin = open("input.txt","r")

n = int(input())
array = list(map(int,input().split()))
s = 0
e = n-1
answer = -1

while s <= e:
    mid = (s+e)//2
    if array[mid] == mid:
        answer = mid 
        break
    elif array[mid] < mid:
        s = mid+1
    else:
        e = mid-1

print(answer)





