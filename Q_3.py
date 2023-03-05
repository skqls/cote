

count0 = 0
count1 = 0
result = 0
array = input()

if array[0] == '0':
    count1 +=1
else:
    count0 +=1

for i in range(len(array)-1):
    if array[i] != array[i+1]:
        if array[i+1] == '0':
            count1 +=1
        else:
            count0 +=1

result = min(count1,count0)
print(result)


    