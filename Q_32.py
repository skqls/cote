import sys
sys.stdin = open("input.txt","r")

n = int(input())

dp = []
for _ in range(n):
    dp.append(list(map(int,input().split())))

#점화식 : dp[i][j] = max(up, left_up) + dp[i][j]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            left_up= 0
        else : left_up = dp[i-1][j-1]
        
        if j == i :
            up = 0
        else :
            up = dp[i-1][j]

        dp[i][j] = max(up, left_up) + dp[i][j]

print(max(dp[n-1]))
