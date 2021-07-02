import sys
sys.stdin = open('input/3273.txt')

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
new_arr = set(arr)
cnt=0

for i in range(n-1):
    num = x - arr[i]

    if num == arr[i]:
        continue
    if num in new_arr:
        new_arr.discard(num)
        new_arr.discard(arr[i])
        cnt+=1
print(cnt)