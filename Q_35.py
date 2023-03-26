import sys
sys.stdin = open("input.txt","r")

n = int(input())

dp = [0]*1001
dp[1]= 1

count2=count3=count5 = 1

value2=2
value3=3
value5=5

for i in range(2,n+1):
    dp[i] = min(value2,value3,value5)
    if dp[i] == value2:
        count2+=1
        value2 = count2*2
    
    if dp[i] == value3:
        count3+=1   
        value3 = count3*2

    if dp[i] == value5:
        count5+=1   
        value5 = count5*2
print(dp[n])


    
        

