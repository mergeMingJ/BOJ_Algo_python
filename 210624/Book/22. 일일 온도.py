# outs: [1,1,4,2,1,1,0,0]

Temp = [73, 74, 75, 71, 69, 72, 76, 73]
result = []
cnt = 0

Temp.append(0);

for i in range(len(Temp)-1):
    cnt= 1
    for j in range(i+1, len(Temp)):
        if Temp[i] < Temp[j]:
            break
        elif j == (len(Temp)-1):
            cnt = 0
        else:
            cnt += 1

    result.append(cnt)
print(result)

