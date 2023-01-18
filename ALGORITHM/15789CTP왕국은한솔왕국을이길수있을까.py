from collections import Counter
from itertools import combinations
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
root = [i for i in range(0, N+1)]

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(a, b):
    A = find(a)
    B = find(b)
    if A > B:
        root[A] = B
    else:
        root[B] = A

def trim():
    for i in root:
        find(i)

for i in range(M):
    a, b = map(int, input().split())
    union(a, b)
    # root = [0, 1, 1, 1, 1, 5, 5, 7, 8, 7, 8]

trim()
# root = [0, 1, 1, 1, 1, 5, 5, 7, 8, 7, 8]

root.pop(0)

CTP, enemy, K = map(int, input().split())
CTP, enemy = CTP - 1, enemy - 1

CTP = root[CTP]
enemy = root[enemy]

# CTP 가 새로 동맹을 맺을 수 없는
# CTP 와의 동맹국, 한솔왕국과의 동맹국 제외하기
root_tmp = [i for i in root if i not in (CTP, enemy)]
# [1, 1, 1, 1, 8, 8]
root_cnt = list(Counter(root_tmp).most_common())
# [(1, 4), (8, 2)]

# print(root)
# print(root_tmp)
# print(root_set)
# print(root_cnt)

# 만약 K 가 더 크다면
# 굳이 다 고를 필요 없으니 len(root_cnt) 로 조정
if len(root_cnt) < K:
    K = len(root_cnt)

answer = 0
idx = 0
for i in root_cnt:
    answer += i[1]
    idx += 1

    if idx == K:
        break

# 크기 순서대로 고른 후, CTP 본인이 가진 동맹국 수 더해주기
print(answer + root.count(CTP))
