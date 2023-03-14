import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline

from itertools import combinations

n,m = map(int,input().split())
houses = []
chickens = []
answer = 1e9

def check_value(datas):
    answer = 0
    for house in houses:
        temp = 0 
        min_value = 1e9
        for chicken in datas:
            temp = abs(house[0]-chicken[0]) + abs(house[1]-chicken[1])
            min_value = min(min_value, temp)
        answer += min_value
    return answer




for i in range(n):
    data = list(map(int,input().split()))
    for j in range(n):
        if data[j] == 1:
            houses.append((i,j))
        elif data[j] == 2:
            chickens.append((i,j))

for datas in list(combinations(chickens,m)):
    value = check_value(datas)
    answer = min(answer, value)

print(answer)



