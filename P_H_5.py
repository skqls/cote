
from collections import defaultdict

def solution(genres, plays):
    
    dict1 = defaultdict(int)
    dict2 = defaultdict(list)
    answer = []
    
    for idx, (data) in enumerate(zip(genres,plays)):
        genre = data[0]
        play = data[1]
        
        dict1[genre] += play
        
        dict2[genre].append((play,idx))
        
    array = sorted(list(dict1.items()), key= lambda x : -x[1] )
    
    while array:
        genre, play = array.pop(0)
        temp = dict2[genre]
        
        temp.sort(reverse = True)
        for i in range(2):
            if len(temp) >0:
                answer.append(temp.pop(0)[1])
    
    return answer
                
        
    
    
    
    
    
    
    