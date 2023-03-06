def solution(s):
    answer = 1e9
    for step in range(1,(len(s)//2)+1):
        prev = s[:step]
        count = 1
        result = ""
        for i in range(step,len(s),step):
            if prev == s[i:i+step]:
                count += 1
            else:
                result += str(count)+prev if count>=2 else prev
                prev = s[i:i+step]
                count = 1
        result += str(count)+prev if count>=2 else prev
        answer = min(answer, len(result))
    
    print(answer)
        
                

s = "aabbaccc"	
solution(s)

    
    
    
    
    
    
    
    
