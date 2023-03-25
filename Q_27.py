import sys
sys.stdin = open("input.txt","r")

from bisect import bisect_left, bisect_right

n,x = map(int,input().split())

data = list(map(int,input().split()))

def count_number_by_range(array, left_target, right_target):
    
    
    left_idx = bisect_left(array, left_target)
    
    right_idx = bisect_right(array, right_target)
    
    return right_idx - left_idx

answer = count_number_by_range(data,x,x)

print(answer) if answer != 0 else print(-1)

