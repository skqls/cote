import sys
sys.stdin = open("input.txt","r")

n = int(input())
array = []
for i in range(n):
    data = list(input().split())
    array.append(data)

array.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for i in range(n):
    print(array[i][0])



