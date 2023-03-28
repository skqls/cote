#dfs
    
def solution(tickets):
    answer = []
    
    used_tickets = [False]*len(tickets)
    
    def dfs(now, visited):
        if len(visited) == len(tickets)+1:
            answer.append(visited)
            return
        
        for idx, ticket in enumerate(tickets):
            if now == ticket[0] and used_tickets[idx] == False:
                used_tickets[idx] = True
                dfs(ticket[1], visited+[ticket[1]])
                used_tickets[idx] = False
                
    dfs("ICN", ["ICN"])
    
    answer.sort()

    return answer[0]






