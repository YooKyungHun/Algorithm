from itertools import combinations

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]



houses, chickens = [], []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            houses.append((i, j))
        elif arr[i][j] == 2:
            chickens.append((i, j))

answer = float("INF")
for comb in combinations(chickens, M):

    city_to_chick = 0
    for house in houses:
        house_x, house_y = house

        house_to_chick = 101
        for i in comb:
            chick_x, chick_y = i
            tmp = abs(house_x - chick_x) + abs(house_y - chick_y)
            house_to_chick = min(house_to_chick, tmp)

        city_to_chick += house_to_chick

    answer = min(answer, city_to_chick)

print(answer)