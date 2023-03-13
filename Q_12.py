def check_proper(array):
    for x,y,a in array:
        if a == 0:
            if y == 0 or [x-1,y,1]in array or [x,y,1] in array or [x,y,-1,0]in array:
                continue
            
            return False

        else :
            if [x,y,-1,0] in array or [x+1,y-1,0] in array or ([x-1,y,1] in array and [x+1,y ,1] in array):
                continue
             
            return False
    return True


def solution(n, build_frame):
    array = []
    for x,y,a,b in build_frame:
        if b == 1 :
            array.append([x,y,a])
            if not check_proper(array):
                array.remove([x,y,a])

        else : 
            array.remove([x,y,a])
            if not check_proper(array):
                array.append([x,y,a])
        
    print(sorted(array))






    
    
    
    
    
    






















n = 5
build_frame =  [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]
solution(n, build_frame)