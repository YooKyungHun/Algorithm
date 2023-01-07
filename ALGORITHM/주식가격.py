from collections import deque


def solution(prices):
    answer = []

    for i in range(len(prices) - 1):
        flag = 0

        for j in range(i + 1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j - i)
                flag = 1
                break
        if flag == 0:
            answer.append(len(prices) - (i + 1))

    answer.append(0)
    return answer