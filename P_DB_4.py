from collections import deque

def solution(begin, target, words):

    if target not in words:
        return 0
    else : 
        length = len(begin)
        words.insert(0,begin)
        graph = [[]for _ in range(len(words))]

        for i in range(len(words)):
            for j in range(len(words)):
                count = 0
                for k in range(length):
                    if words[i][k] == words[j][k]:
                        count += 1
                    else:
                        continue
                if count == (length - 1):
                    graph[i].append(j)

        q = deque([0])
        dist = [0]* len(words)
        while q :
            now = q.popleft()
            for i in graph[now]:
                if dist[i] == 0 :
                    dist[i] = dist[now] + 1
                    q.append(i)
        
        idx = words.index(target)
        return dist[idx]