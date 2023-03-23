def solution(n, computers):

    def dfs(now):
        visited[now] = True
        data = computers[now]
        for i in range(n):
            if data[i] == 1 and not visited[i]:
                dfs(i)
        return True

    count = 0
    visited = [False] * n
    for now in range(n):
        if not visited[now] and dfs(now):
            count += 1

    return count