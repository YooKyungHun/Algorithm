n = int(input())

tree = [list(map(int, input())) for _ in range(n)]
# [1, 1, 1, 1, 0, 0, 0, 0],
# [1, 1, 1, 1, 0, 0, 0, 0],
# [0, 0, 0, 1, 1, 1, 0, 0],
# [0, 0, 0, 1, 1, 1, 0, 0],
# [1, 1, 1, 1, 0, 0, 0, 0],
# [1, 1, 1, 1, 0, 0, 0, 0],
# [1, 1, 1, 1, 0, 0, 1, 1],
# [1, 1, 1, 1, 0, 0, 1, 1]]

def func(x, y, n):
    tmp = tree[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if tmp != tree[i][j]:
                new_n = n//2
                print('(', end='')
                func(x, y, new_n)
                func(x, y + n//2, new_n)
                func(x + n//2, y, new_n)
                func(x + n//2, y + n//2, new_n)
                print(')', end='')
                return

    # 현재 배열 단위를 하나의 값으로 나타낼 수 있는 경우
    if tmp == 0:
        print(0, end="")
    elif tmp == 1:
        print(1, end="")
func(0, 0, n)
