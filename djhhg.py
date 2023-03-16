def solution(k, user_scores):
    answer = 0
    array = []
    
    for user_score in user_scores:
        nickname, score = user_score.split()
        score = int(score)
        found = False
        
        # Check if the user has a previous score
        for i, data in enumerate(array):
            if data[1] == nickname:
                found = True
                
                # Update the user's score if the new score is higher
                if score > data[0]:
                    array[i] = (score, nickname)
                    array.sort(key=lambda x: (-x[0], x[2]))
                    break
        
        # Add the user's score if it's the first time
        if not found:
            array.append((score, nickname, len(array)))
            array.sort(key=lambda x: (-x[0], x[2]))
        
        # Calculate the number of times the ranking page changes
        if len(array) <= k:
            if answer != len(array):
                answer = len(array)
        else:
            if array[k - 1] != array[k]:
                answer += 1
    
    return answer


k = 3
user_scores = [
    "alex111 100",
    "cheries2 200",
    "coco 150",
    "luna 100",
    "alex111 120",
    "coco 300",
    "cheries2 110",
]
result = solution(k, user_scores)
print(result)  # Output: 4
