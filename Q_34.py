import sys
sys.stdin = open("input.txt","r")

n = int(input())
array = list(map(int,input().split()))

array.reverse()
array.insert(0,0)

dp = [0]*(n+1)

for i in range(1,n+1):
    for j in range(i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n-max(dp))



    