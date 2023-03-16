import sys
sys.stdin = open("input.txt","r")

for tc in range(int(input())):
    n,m = map(int,input().split())
    dp = []
    data = list(map(int,input().split()))
    for start in range(0,n*m,m):
        dp.append(data[start:start+m])
    
    
    

    for j in range(1,m):
        for i in range(n):
            if i == 0 :
                left_up = 0
            else : left_up = dp[i-1][j-1]
            
            if i == n-1:
                left_down = 0
            else : left_down = dp[i+1][j-1]

            left = dp[i][j-1]
            dp[i][j] = max(left_up,left,left_down)+dp[i][j]
    
    max_value = -(1e9)
    for i in range(n):
        if dp[i][m-1] > max_value :
            max_value = dp[i][m-1]
    
    print(max_value)







     


