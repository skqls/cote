import sys
sys.stdin = open("input.txt","r")


n = int(input())
time = [0] * (n+1)
price = [0] * (n+1)

dp = [0] * (n+2)
for i in range(n):
    t, p = map(int, input().split())
    time[i] = t
    price[i] = p

max_value = 0

for i in range(n-1, -1, -1):
    temp = time[i]+i
    if temp <= n:
        dp[i] = max(price[i]+dp[temp], max_value)
        max_value = dp[i]

print(max(dp))



