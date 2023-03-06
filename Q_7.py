data = input()
sum_count = 0
for i in range(len(data)//2):
    sum_count += int(data[i])

for j in range(len(data)//2,len(data)):
    sum_count -= int(data[j])

if sum_count == 0 :
    print("LUCKY")
else:
    print("READY")