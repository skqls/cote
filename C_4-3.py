import sys
sys.stdin = open("input.txt","r")


data = input()
answer = 0


row = data[1]
column = ord(data[0]) - ord('a') + 1

move_types = [(-2,-1), (-1,2), (1,-2), (2,-1), (2,1), (1,2), (-1,2),(-2,1)]
result = 0
for move_type in move_types:
    next_row = row + move_types[0]
    next_column = column + move_types[1]
    if next_row >= 1 and next_row < 9 and next_column >=1 and next_column <9 :
        answer +=1

print(answer)