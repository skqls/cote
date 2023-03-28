def solution(participant, completion):



    participant.sort()
    completion.sort()
    for p,c in zip(participant, completion):
        print(p,c)
        if p!=c:
            return p
    return participant[-1]







# def solution(participant, completion):
    
#     participant.sort()
#     completion.sort()
    
#     for a,b in zip(participant,completion):
#         if a != b:
#             return a
#     return participant[-1]