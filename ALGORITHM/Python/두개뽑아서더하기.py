from itertools import combinations


def solution(numbers):
    answer = []

    for comb in combinations(numbers, 2):
        sum_comb = sum(comb)
        answer.append(sum_comb)

    answer = list(set(answer))
    return sorted(answer)