# https://school.programmers.co.kr/learn/courses/30/lessons/42889?language=python3
# 2019 KAKAO BLIND RECRUITMENT
# 실패율


import heapq

def solution(N, stages):
    num = len(stages)
    array = [0]*(N+2)
    for i in stages:
        array[i] += 1
    
    q = []
    failure = 0
    for i in range(1,N+1):
        if num != 0 :
            failure = array[i]/num 
        else :
            failure = 0
        num -= array[i]
        heapq.heappush(q,(-failure,i))
        
    answer = []
    
    while q:
        answer.append(heapq.heappop(q)[1])
    
    return answer