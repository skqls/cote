import sys
sys.stdin = open("input.txt","r")

n,m,k = map(int,input().split())
data = list(map(int,input().split()))
answer = 0

data.sort()
first = data[-1]
second = data[-2]

while m > 1 :
    for i in range(k):
        if m > 0:
            answer += first
            m-=1
    if m > 0 :
        answer += second
        m -= 1

print(answer)