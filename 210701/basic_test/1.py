# 1. 정수 n이 주어졌을 때 7을 삽입해 만들 수 있는 가장 큰 숫자를 리턴하는 함수를 하나 구현
# 정수 n은 -9999 <= n <= 9999 의 범위를 가집니다.
#
# example
# 1294  -> 71294
# -9123 -> -79123


n = list(str(input()))

ans = ''


for i in range(len(n)):
    # 음수일 경우
    if n[0] == '-':
        if i == 0:
            pass
        else:
            if n[i] > '7':
                n.insert(i, '7')
                break
            if i == len(n)-1:
                n.append('7')
    else:
        if n[i] < '7':
            n.insert(i, '7')
            break
        if i == len(n)-1:
            n.append('7')

for char in n:
    ans+=char
print(int(ans))
