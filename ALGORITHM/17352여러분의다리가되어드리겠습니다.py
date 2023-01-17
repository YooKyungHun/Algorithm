import sys

N = int(input())
root = [i for i in range(N+1)]

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

for i in range(N-2):
    a, b = map(int, sys.stdin.readline().split())

    union(a, b)
    # [0, 1, 1, 1, 3, 3, 6, 6, 7]

for i in range(N+1):
    find(i)

# 8
# 1 2
# 3 4
# 3 5
# 7 8
# 6 7
# 5 2
# 전체 find 를 통해 모두 root 를 찾아가도록 조정
# 전체 find(i) 전 root: [0, 1, 1, 1, 3, 3, 6, 6, 7]
# 전체 find(i) 후 root: [0, 1, 1, 1, 1, 1, 6, 6, 6]

# 어차피 다리그룹은 두개밖에 있을 수 없으니
# 1 을 root 로 가지는 idx(1, 2, 3, 4, 5) 중 1개와
# 6 를 root 로 가지는 idx(6, 7, 8) 중 1개를 서로 union 을 해주면 됨
tmp_a = root[1]
for i in range(1, len(root)):
    if tmp_a != root[i]:
        tmp_b = root[i]
        break
print(1, i)

# 어차피 전체 find 후에는 전체 다리의 root 2개만 남기 때문에
# 맨 앞의 0 을 제외한 뒤 출력해도 됨
# root.pop(0)
# print(*set(root))
