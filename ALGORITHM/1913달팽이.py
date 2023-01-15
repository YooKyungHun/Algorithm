N = int(input())
Target = int(input())

arr = [[0] * N for _ in range(N)]

# 초기값 설정
x, y = N // 2, N // 2

# 델타 상 우 하 좌
k = 0
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 초기값 설정
idx = 1
S = 1
answer = []

def func():
    for i in arr:
        print(*i)
    print(*answer)

while True:
    # 상위 for 문은 2번씩
    for i in range(2):
        # S = 1 부터 늘어나도록
        for j in range(S):
            if idx != N**2+1:
                arr[x][y] = idx

                if idx == Target:
                    answer.append(x+1)
                    answer.append(y+1)

                x, y = x + dx[k], y + dy[k]
                idx += 1

            # 종료조건
            else:
                func()
                exit(0)

        # 방향전환
        k += 1
        if k >= 4: k = k % 4

    S += 1

