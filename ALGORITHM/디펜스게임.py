from collections import deque


def solution(n, k, enemy):
    answer = 0
    queue = deque(enemy)
    tmp = deque()

    if len(enemy) <= k: return len(enemy)

    for idx in range(len(queue)):
        # 내 병사 >= 적군 일때 병사 사용:
        if n >= enemy[idx]:
            n = n - enemy[idx]
            tmp.append(enemy[idx])

        # 내 병사 < 적군 일때 무조건 K 사용
        elif n < enemy[idx]:
            # 전에 병사 사용한게 아까워 -> 그거 무조권썻다고 하고 이번엔 병사 사용할래
            if len(tmp) != 0 and max(tmp) > enemy[idx] and k >= 1:
                n += max(tmp)
                tmp.remove(max(tmp))
                k -= 1

                n -= enemy[idx]
                tmp.append(enemy[idx])

            # tmp 가 비었거나 max(tmp) <= enemy[idx] 라서 그냥 지금 무조권쓰는게 나음
            elif k >= 1 and (len(tmp) == 0 or max(tmp) <= enemy[idx]):
                k -= 1

            # 종료조건: 적군이 더 많은데 K 도 없어
            elif k == 0:
                return answer

        answer += 1
    return answer


# print(solution(2, 4, [3,3,3,3]))
# # 4
# print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
# 5
# print(solution(7, 3, [5, 5, 5, 5, 2, 3, 1]))
# ans : 5
# print(solution(1, 6, [2, 2, 2, 2, 3, 3, 1]))
# # ans : 7
# print(solution(10, 1, [2, 2, 2, 2, 2, 10]))
# # ans : 6
# print(solution(10, 1, [2, 2, 2, 2, 10]))
# # ans : 5