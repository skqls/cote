

def solution(key, lock):
    
    def rotate_by_90_degree(key):
        temp = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                temp[j][n-i-1] = key[i][j]
        return temp
    
    def check_new_lock(new_lock):
        for i in range(m,2*m):
            for j in range(m,2*m):
                if new_lock[i][j] != 1:
                    return False
        return True

    n = len(key)
    m = len(lock)
    
    new_lock = [[-1]*(3*m)for _ in range(3*m)]
    for i in range(m):
        for j in range(m):
            new_lock[m+i][m+j] = lock[i][j]
    
    for _ in range(4):
        key = rotate_by_90_degree(key)
        for i in range(2*m):
            for j in range(2*m):
                for x in range(n):
                    for y in range(n):
                        new_lock[i+x][j+y] += key[x][y]
                if check_new_lock(new_lock):
                    return True
                for x in range(n):
                    for y in range(n):
                        new_lock[i+x][j+y] -= key[x][y]
    return False
                
    
    
    
    
