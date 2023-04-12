def solution(park, routes):
    N, M = len(park), len(park[0])

    direct = {"E": (0, 1), "W": (0, -1), "N": (-1, 0), "S": (1, 0)}

    for i in range(N):
        for j in range(M):
            if park[i][j] == "S":
                now_x, now_y = i, j
                break

    for route in routes:
        direction, distance = map(str, route.split())
        distance = int(distance)
        dx, dy = direct[direction]

        flag = 1
        for i in range(1, distance + 1):
            next_x = now_x + dx * i
            next_y = now_y + dy * i

            if 0 > next_x or next_x >= N or 0 > next_y or next_y >= M or park[next_x][next_y] == 'X':
                flag = 0
                break
        if flag == 0:
            continue

        now_x, now_y = next_x, next_y

        '''
        중간에 장애물이 있는 경우 -> continue
        중간에 범위 밖인 경우 -> continue
        '''

    return (now_x, now_y)