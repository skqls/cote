def dfs(count, data, target, numbers):
    answer = 0
    
    if count == len(numbers):
        if data == target:
            answer += 1
    else:
        answer += dfs(count+1, data+numbers[count], target, numbers)
        answer += dfs(count+1, data-numbers[count], target, numbers)

    return answer

def solution(numbers, target):
    answer = dfs(0, 0, target, numbers)
    return answer