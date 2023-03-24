def solution(s):
    data = s.split()

    max_value = -(1e9)
    min_value = 1e9
    
    for i in data :
        max_value = max(max_value, int(i))
        min_value = min(min_value, int(i))
    
    return str(min_value) + " " + str(max_value)
    