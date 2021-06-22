import sys
sys.stdin = open('input/10815.txt', 'r')

N = int(input())
n_lst = list(map(int, input().split()))
M = int(input())
m_lst = list(map(int, input().split()))

# dictionary 형식으로
result = dict()

# key가 m이고 value가 0 인 딕셔너리 만들기
for m in m_lst:
    result[m] = 0

# n이 result의 key와 같으면 key[n]=1
for n in n_lst:
    if n in result:
        result[n] = 1

    # 이건 시간 초과
    # for re in result:
    #     if re == n:
    #         result[n]=1

for dap in result.values():
    print(dap, end=" ")


