import sys
sys.stdin = open("input.txt","r")

n,c = map(int, input().split())
array = []
for _ in range (n):
    array.append(int(input()))

array.sort()
answer = 0
def binary_search(array, s,e):
    global answer
    if s > e :
        return

    mid = (s+e) //2
    value = array[0]
    count = 1
    
    for i in range(1,n):
        if array[i] > value + mid :
            count += 1
    
    if count >= c :
        answer = count
        return binary_search(array,mid+1,e)
    else :
        return binary_search(array,s,mid-1)

binary_search(array, 0 , n-1)
print(answer)


            


        