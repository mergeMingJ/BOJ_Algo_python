import sys
sys.stdin = open('input/1292.txt', 'r')

A, B = map(int, input().split())
num_lst = []
hap = 0

# 1 ≤ A ≤ B ≤ 1000 => 1~46의 합이 1035
for i in range(1, 47):
    for j in range(i):
        num_lst.append(i)


# 구간 합 구하기
for s in range(A-1, B):
    hap += num_lst[s]

print(hap)


