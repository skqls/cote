# 2019 KAKAO BLIND RECRUITMENT


import heapq

def solution(food_times, k):
    
    
    if sum(food_times) <= k :
        return -1
    else :
        
        q = []
        for i in range(len(food_times)):
            heapq.heappush(q,(food_times[i],i+1))
        
        length = len(food_times)
        prev = 0 
        sum_num = 0
        
        while ((q[0][0]-prev)*length + sum_num) <= k :
            now = heapq.heappop(q)[0]
            sum_num += (now-prev)*length
            length -= 1
            prev = now
            
        q.sort(key = lambda x : x[1])
        k -= sum_num
        return q[(k%length)][1]
        
        
# food_times = [3, 1, 2]
# k = 5
# solution(food_times, k)