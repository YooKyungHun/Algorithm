from collections import deque


def solution(n, k, enemy):
    answer = 0
    queue = deque(enemy)
    tmp = [-1]
    idx = 0

    while n > 0 or k > 0:

        # 내 병사 < 적군
        if n < queue[idx]:
            # 내가 무적권 사용하지 않았을때 가장 큰 적군 < 지금 적군
            if max(tmp) <= queue[idx]:
                k = k - 1
            else:
                n = n + max(tmp)  # 병사 부활
                k += 1
                tmp.remove(max(tmp))

                n = n - queue[idx]
                k -= 1
                k -= 1
                tmp.append(queue[idx])

        # 내 병사 >= 적군
        else:
            if n < queue[idx]:
                return answer

            n = n - queue[idx]
            tmp.append(queue[idx])

        answer += 1
        idx += 1
    return answer

print(solution(7, 3, [4, 2, 4, 5, 3, 3, 1]))
