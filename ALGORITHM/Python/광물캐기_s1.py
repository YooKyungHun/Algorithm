from collections import deque


def solution(picks, minerals):
    answer = 0

    # 전처리 - 1
    # TC 2 (곡괭이 수 * 5 보다 미네랄이 더 많아서, 모두 캐지 못할 경우)
    if sum(picks) * 5 < len(minerals):
        minerals = minerals[0:sum(picks) * 5]

    # 전처리 - 2
    # TC 1 (곡괭이가 너무 많은 경우)
    else:
        # 나머지가 있다면
        if len(minerals) % 5:
            필요한곡괭이수 = len(minerals) // 5 + 1
        # 5의 배수일 때
        else:
            필요한곡괭이수 = len(minerals) // 5

        for i in range(sum(picks) - 필요한곡괭이수):
            if picks[2]:
                picks[2] -= 1
            elif picks[1]:
                picks[1] -= 1
            elif picks[0]:
                picks[0] -= 1
        # picks = [1, 1, 0]

    minerals = deque(minerals)

    # 미네랄 5개씩 끊기
    all_minerals = []
    while minerals:
        times = 5
        if len(minerals) < 5:
            times = len(minerals)

        five_min = [0, 0, 0]
        for i in range(times):
            tmp = minerals.popleft()
            if tmp == "diamond":
                five_min[0] += 1
            elif tmp == "iron":
                five_min[1] += 1
            elif tmp == "stone":
                five_min[2] += 1
        all_minerals.append(five_min)
    # all_minerals = [[3, 2, 0], [1, 1, 1]]
    # all_minerals = [[5, 0, 0], [0, 5, 0]]

    # 5개씩 끊은 미네랄을 피로도로 바꾸기
    all_cost = []
    for dia, iron, stone in all_minerals:
        five_cost = []
        # 다이아 곡괭이로 채광
        five_cost.append(dia + iron + stone)  # sum(i)
        # 철 곡괭이로 채광
        five_cost.append(5 * dia + iron + stone)
        # 돌 곡괭이로 채광
        five_cost.append(25 * dia + 5 * iron + stone)

        all_cost.append(five_cost)

    # 각 곡괭이로 채광시 소모되는 피로도: [dia, iron, stone]
    # [[5, 17, 85], [3, 7, 31]]
    # [[5, 25, 125], [5, 5, 25]]

    all_cost.sort(key=lambda x: (-x[2], -x[1], -x[0]))
    all_cost = deque(all_cost)

    for cost in all_cost:
        dia, iron, stone = cost

        for i in range(3):
            if i == 0 and picks[0]:
                picks[0] -= 1
                answer += dia
                print(dia)
                break

            if i == 1 and picks[1]:
                picks[1] -= 1
                answer += iron
                print(iron)
                break

            if i == 2 and picks[2]:
                picks[2] -= 1
                answer += stone
                print(stone)
                break

    return answer

