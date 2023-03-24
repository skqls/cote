import heapq

n = int(input())

heap = []
for i in range(n):
    heapq.heappush(heap,(int(input())))

answer = 0

while len(heap) > 1:
    first = heapq.heappop(heap)
    second = heapq.heappop(heap)
    
    temp = first + second
    answer += temp
    heapq.heappush(heap,temp)

print(answer)