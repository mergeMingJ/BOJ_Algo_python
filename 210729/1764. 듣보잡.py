import sys
sys.stdin = open('input/1764.txt', 'r')

N, M = map(int, input().split())

lst = {}
cnt = 0
ans = []
for n in range(N):
    person = input()
    lst[person] = 1
for m in range(M):
    person = input()
    if person not in lst.keys():
        lst[person] = 1
    else:
        lst[person] += 1
        cnt+=1

print(cnt)
for key, value in lst.items():
    if value > 1:
        ans.append(key)
answer = sorted(ans)
for a in answer:
    print(a)

# 시간초과
# lst = []
# cnt = 0
# ans_lst = []
#
# for n in range(N):
#     person = input()
#     lst.append(person)
# for m in range(M):
#     person = input()
#     if person in lst:
#         cnt+=1
#         ans_lst.append(person)
# print(cnt)
# ans = sorted(ans_lst)
# for a in ans:
#     print(a)
