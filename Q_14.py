from itertools import permutations

def solution(n, weak, dist):
    answer = 1e9
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    
    for start in range(length):
        for friends in list(permutations(dist,len(dist))):
            count = 1
            pos = weak[start] + friends[count-1]
            for i in range(start, start+length):
                if weak[i] > pos:
                    count += 1
                    if count > len(dist):
                        break
                    else:
                        pos = weak[i] + friends[count-1]
            answer = min(answer,count) 
    
    if answer != 1e9:
        print(answer )
    else :
        print(-1)





















n= 12
weak = [1,5,6,10]
dist = [1,2,3,4]
solution(n, weak, dist)