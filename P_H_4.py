



from collections import defaultdict

def solution(clothes):
    data = defaultdict(list)
    for cloth in clothes:
        if cloth[0] not in data[cloth[1]]:
            data[cloth[1]].append(cloth[0])
 
    temps = list(data.values())
    for temp in temps :
        answer *= (len(temp)+1)
    return answer-1




# def solution(clothes):
#     data = dict()
    
#     for cloth in clothes :
#         if cloth[1] in data.keys():
#             data[cloth[1]]+=1
#         else : 
#             data[cloth[1]] = 1
    
#     value = list(data.values())
    
#     answer = 1
#     for i in range(len(value)):
#         answer *= (value[i]+1)
#         print(answer)
    
#     return (answer -1)
            