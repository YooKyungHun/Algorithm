from itertools import permutations, combinations

def solution(k, dungeons):
    count_dungeons = []
    for perm in permutations(range(len(dungeons))):
        # 012, 021, 102, 120, 201, 210
        cnt = 0
        health = k

        for i in perm:
            # 체력 >= 최소 필요 피로도: 방문 후 체력 소모
            if health >= dungeons[i][0]:
                health = health - dungeons[i][1]
                # print('health : ', health)
                cnt += 1

            # 체력 < 최소 필요 피로도: 방문 불가능
            else:
                break
        count_dungeons.append(cnt)

    return max(count_dungeons)
