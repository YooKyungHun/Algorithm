import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline

def find(x):
    if root[x] != x:
        root[x] = find(root[x])

    return root[x]

def union(x, y):
    X = find(x)
    Y = find(y)

    if X < Y:
        root[Y] = X
    else:
        root[X] = Y

    # ex) 5 -> 3, 7 -> 2 일때
    # union(5, 7) 하면
    # 3(Y) -> 2(X) 해해야함.

    # ex) 3 -> 1, 7 -> 6 일때
    # union(3, 7) 하면
    # 7(y) -> 1(X) 하면 6 은 하나의 집합에 포함이 안됨.
    # 6(Y) -> 1(X) 해야 함.

n, op_num = map(int, input().split())
root = [i for i in range(n + 1)]
for _ in range(op_num):
    op, x, y = map(int, input().split())
    if op == 0:
        union(x, y)
    else:
        print('YES' if find(x) == find(y) else 'NO')