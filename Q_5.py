import sys
sys.stdin = open("input.txt","r")

from collections import defaultdict

data = defaultdict(int)


n, m = map(int,input().split())
array = list(map(int,input().split()))

for x in array :
    data[x] += 1

result = 0
data = list(data.values())

for i in data:
    n -= i
    result += (i*n)

print(result)
    