import sys

N, r, c = map(int, input().split())
cnt = 0
def func(x, y, N):
    global cnt

    # 찾고자하는 (r, c) 가 현재 탐색중인 사각형 밖에 있는 경우,
    # 그 사각형의 넓이(N**2) 만큼 cnt 에 더해주기
    if x>r or x+N <= r or y>c or y+N <= c:
        cnt += N**2
        return

    if N > 2:
        new_N = N // 2
        func(x        , y        , new_N)
        func(x        , y + new_N, new_N)
        func(x + new_N, y        , new_N)
        func(x + new_N, y + new_N, new_N)

    # 가장 작은 사각형 단위 2*2 중에 (r, c) 가 있는 경우
    else:
        if x == r and y == c:
            print(cnt)
        elif x == r and y + 1 == c:
            print(cnt + 1)
        elif x + 1 == r and y == c:
            print(cnt + 2)
        else:
            print(cnt + 3)
        sys.exit()
func(0, 0, 2**N)