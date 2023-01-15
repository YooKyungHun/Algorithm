def find(x):
    if root[x] != x:
        root[x] = find(root[x])

    return root[x]
    """
    1, 2, 3, 4, 5

    (1,2,3,4,5)  
    """


def union(x, y):
    # 0 1 2 3 4 5
    # [ 1 1 2 3 4]
    X = find(x)  # x =5 , 5->1, 4->1, 3->1, 2->1  y = 1  O(N)
    Y = find(y)

    if X < Y:
        root[y] = X
    else:
        root[x] = Y


n, op_num = map(int, input().split())
root = [i for i in range(n + 1)]
for _ in range(op_num):
    op, x, y = map(int, input().split())
    if op == 0:
        union(x, y)
    else:
        print('YES' if find(x) == find(y) else 'NO')