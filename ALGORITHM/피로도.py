from itertools import permutations
def solution(k, dungeons):
    answer = -1

    tmp = []
    for perm in permutations(range(len(dungeons))):
        cnt = 0  # 012, 021, 102, 120, 201, 210
        health = k
        # print(health)

        for i in perm:
            if health >= dungeons[i][0]:
                health = health - dungeons[i][1]
                # print('health : ', health)
                cnt += 1
            else:
                break
        tmp.append(cnt)
    # print(tmp)

    return max(tmp)