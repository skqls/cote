import sys
sys.stdin = open("input.txt","r")

s = input()
s = list(s)
alpha = []
count = 0
for x in s :
    if x.isalpha() :
        alpha.append(x)
    else :
        count+=int(x)

alpha.sort()
answer = ""

answer += "".join(alpha)
if count != 0 :
    answer += str(count)
print(answer)
