N, H, D = map(int, input().split())
arr = [list(input()) for _ in range(N)]
# [['S', '.', '.', 'U'],
#  ['.', '.', '.', '.'],
#  ['.', '.', '.', '.'],
#  ['.', '.', '.', 'E']]

umbrella = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'S': stateX, stateY = i, j
        elif arr[i][j] == 'E': safeareaX, safeareaY = i, j
        elif arr[i][j] == 'U': umbrella.append([i, j])

# 우산 개수만큼 visited 배열 생성
visited = [0] * len(umbrella)

answer = float("inf")

# x, y: 현재 위치
# H, umb: 체력, 현재 우산의 내구도
# res: 처음 위치부터 현재 위치까지의 거리
def DFS(x, y, H, umb, res):
    global answer

    # 종료조건
    if umb <= 0 and H <= 0:
        return

    # 우산을 추가로 방문할 필요없이 곧바로 종료지점으로 갈 수 있는 경우
    distToSafearea = abs(x - safeareaX) + abs(y - safeareaY)
    if distToSafearea <= H + umb:
        answer = min(answer, res + distToSafearea)
        return

    else:
        # 다음 방문할 우산 찾기
        for i in range(len(umbrella)):
            # 현재 위치에서부터 우산까지의 거리
            dist = abs(x - umbrella[i][0]) + abs(y - umbrella[i][1])

            # 다음 우산까지의 거리가 너무 먼 경우 or 방문한 우산인 경우
            if (H + umb < dist or visited[i] == 1):
                continue

            # 우산의 내구도가 없는 경우: 체력(H) 사용, 새 우산 획득(우산 자리에서도 내구도 1 감소)
            if umb == 0:
                # 현재 체력
                # = 현재 체력 - (거리까지 소요되는 체력)
                # = 현재 체력 - (거리 - 1)
                H = H - (dist - 1)
                umb = D - 1

            # 우산의 내구도가 다음 우산까지 가려면 부족한 경우: 체력(H) 사용, 새 우산 획득(우산 자리에서도 내구도 1 감소)
            elif umb < dist:
                # 현재 체력
                # = 현재 체력 - (거리까지 소요되는 체력 - 사용한 우산의 내구도)
                # = 현재 체력 - (거리 - 1 - 사용한 우산의 내구도)
                H = H - (dist - umb - 1)
                umb = D - 1

            # 우산의 내구도가 다음 우산까지 거리만큼 충분한 경우: 우산의 내구도(umb) 사용, 새 우산 획득(우산 자리에서도 내구도 1 감소)
            elif umb >= dist:
                H = H
                umb = D - 1

            visited[i] = 1
            DFS(umbrella[i][0], umbrella[i][1], H, umb, res + dist)
            visited[i] = 0


DFS(stateX, stateY, H, 0, 0)
print(-1 if answer == float("inf") else answer)
