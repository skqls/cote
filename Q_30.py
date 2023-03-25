
from bisect import bisect_left, bisect_right




def count_by_range(array, left, right):
    left_idx = bisect_left(array, left)
    right_idx = bisect_right(array, right)
    return right_idx - left_idx


def solution(words, queries):
    answer = []

    array =  [[] for _ in range(10001)]
    reversed_array = [[] for _ in range(10001)]

    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    
    for query in queries :
        if query[0] != '?':
            data =count_by_range(array[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
            answer.append(data)
        else :
            data =count_by_range(reversed_array[len(query)], query[::-1].replace('?', 'a'), query[::-1].replace('?', 'z'))
            answer.append(data)

    return answer






