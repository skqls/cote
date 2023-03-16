from collections import defaultdict

def solution(nums):
    data = defaultdict(int)
    
    for i in nums:
        data[i] += 1
        
    length = len(list(data.keys()))
    if length >= (len(nums)/2):
        return (len(nums)/2)
    else : 
        return length