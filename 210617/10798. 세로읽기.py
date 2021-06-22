import sys
sys.stdin = open('input/10798.txt', 'r')

# 미리 최대 크기의 빈 배열 만들어 놓음
arr = [['' for _ in range(15)] for _ in range(5)]
lst = [[k for k in ('').join(input().split())] for _ in range(5)]
result = ''

# 빈 배열에 input 값 입력 받기
for i in range(5):
    for j in range(len(lst[i])):
        arr[i][j] = lst[i][j]

# 세로 출력
for i in range(15):
    for j in range(5):
        result += arr[j][i]
print(result)

