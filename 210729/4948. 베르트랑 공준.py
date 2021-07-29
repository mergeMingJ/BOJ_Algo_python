import sys
sys.stdin = open('input/4948.txt', 'r')

N = 123456 * 2 + 1
prime = [True] * N
for i in range(2, int(N**0.5)+1):
    if prime[i]:
        for j in range(2*i, N, i):
            prime[j] = False

def prime_cnt(val):
    cnt = 0
    for i in range(val + 1, val * 2 + 1):
        if prime[i]:
            cnt += 1
    print(cnt)

while True:
    val = int(input())
    if val == 0:
        break
    prime_cnt(val)