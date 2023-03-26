import sys
sys.stdin = open("input.txt","r")
input = sys.stdin.readline


n, s = map(int, input().split())
array = list(map(int, input().split()))
visited = [False] * n
answer = set()

def dfs(data, curr_sum):
    if curr_sum == s:
        answer.add(tuple(sorted(data)))
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            data.append(array[i])
            dfs(data, curr_sum + array[i])
            data.pop()
            visited[i] = False

dfs([], 0)
print(len(answer))
