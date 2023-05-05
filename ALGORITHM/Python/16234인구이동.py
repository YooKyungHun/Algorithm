from collections import deque

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 델타 상 좌 하 우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def BFS(a, b):
    global flag
    queue = deque()
    queue.append([a, b])

    tmp = []
    tmp.append([a, b])
    tmp_sum = arr[a][b]

    visited[a][b] = 1

    while queue:
        x, y = queue.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and L <= abs(arr[x][y] - arr[nx][ny]) <= R and visited[nx][ny] == 0:
                queue.append([nx, ny])
                tmp.append([nx, ny])
                tmp_sum += arr[nx][ny]
                # 열린 국경에 대해서 visited 처리를 해줌으로써
                # 그 나라에는 다시 방문할 필요가 없음
                visited[nx][ny] = 1

    # while 문을 다 끝내고 나면
    # tmp 에서 인구이동 시작
    if len(tmp) > 1:
        flag = 1
        for a, b in tmp:
            arr[a][b] = tmp_sum//len(tmp)

answer = 0
while True:
    # 이중 for 문 전체 1번이 인구이동을 할 수 있는 날짜 1일(anwser) 에
    # 해당하는 개념이므로 매일 flag 와 visited 를 최신화시켜줌
    # flag 는 1이면 그 날은 인구이동은 한 것.
    # 인구이동은 안한 상태(flag == 0) 로 하루가 끝나면(while 문 1번)
    # 종료조건 충족
    flag = 0
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                BFS(i, j)

    if flag != 0:
        answer += 1

    # 이중 for 문을 전부 돌았는데도 불구하고
    # flag 가 0 이라면(=인구이동을 전혀하지 않았다면)
    # 국경이 열린게 없다는 의미이므로 break
    if flag == 0:
        break

print(answer)

