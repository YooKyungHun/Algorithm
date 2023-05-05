from itertools import combinations

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

houses = []
chicken = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            houses.append([i, j])
        if arr[i][j] == 2:
            chicken.append([i, j])

def func(comb):
    for a, b in houses:

        # 각 집에서 치킨거리
        min_dist = N * 2
        for x, y in comb:
            dist = abs(a - x) + abs(y - b)
            if min_dist > dist:
                min_dist = dist
        distance.append(min_dist)

    # 도시의 치킨거리
    city.append(sum(distance))

city = []  # 치킨집 조합마다 도시의 치킨거리
for comb in combinations(chicken, M):
    # ([0, 1], [3, 0])

    distance = []  # 각 집의 치킨거리
    func(list(comb))

print(min(city))