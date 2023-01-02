import sys
input = sys.stdin.readline

N, M = map(int, input().split())

N_set = set([input() for i in range(N)])

cnt = 0
for i in range(M):
    if input() in N_set:
        cnt += 1

print(cnt)