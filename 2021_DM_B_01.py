def solution(lottos, win_nums):
    zero = 0
    array = []
    win_nums = set(win_nums)
    
    for i in lottos:
        if i == 0:
            zero += 1
        else :
            array.append(i)
    count = 0
    for j in array : 
        if j in win_nums :
            count += 1
    
    max_num = count + zero
    min_num = count 
    answer = []
    
    if max_num == 6 :
        answer.append(1)
    elif max_num == 5 : answer.append(2)
    elif max_num == 4 : answer.append(3)
    elif max_num == 3 : answer.append(4)
    elif max_num == 2 : answer.append(5)
    else : answer.append(6)
    
    if min_num == 6 :
        answer.append(1)
    elif min_num == 5 : answer.append(2)
    elif min_num == 4 : answer.append(3)
    elif min_num == 3 : answer.append(4)
    elif min_num == 2 : answer.append(5)
    else : answer.append(6)
    
    return(answer)
    
        
    
    
  