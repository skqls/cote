import sys
sys.stdin = open("input.txt","r")


n, x = map(int,input().split())
array = list(map(int,input().split()))




def find_left(array,left_target,start,end):

    if start > end:
        return None
    mid = (start+end) //2

    if (mid == 0 or array[mid] != array[mid-1]) and array[mid] == left_target :
        return mid
    elif array[mid]>=left_target:
        return find_left(array,left_target,start,mid-1)
    else: return find_left(array,left_target, mid+1, start)

def find_right(array,right_target,start,end):

    if start > end:
        return None
    mid = (start+end) //2

    if (mid == (n-1) or array[mid] != array[mid+1]) and array[mid] == right_target :
        return mid
    elif array[mid]>=right_target:
        return find_right(array,right_target,start,mid-1)
    else: return find_right(array,right_target, mid+1, start)



def count_by_range(array, left_target, right_target):
    n = len(array)
    a = find_left(array,x, 0, n-1)
    if a == None:
        return 0

    b = find_right(array,x,0,n-1)

    return b-a+1

count = count_by_range(array,x)

if count == 0:
    print(-1)
else : print(count)
