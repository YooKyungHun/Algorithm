from itertools import combinations

def solution(numbers, target):
    answer = 0
    sum_num = sum(numbers)
    numbers.sort(reverse=True)

    if sum_num == target: return 1

    for i in range(1, len(numbers) + 1):
        for comb in combinations(numbers, i):
            # print(comb)
            # 각 요소에 - 를 준다는 방향으로
            # (4,), (2,), (1,), (1,),
            # (4, 2), (4, 1), (4, 1), (2, 1), (2, 1), (1, 1),
            # (4, 2, 1), (4, 2, 1), (4, 1, 1), (2, 1, 1),
            # (4, 2, 1, 1)

            # ex) 4 에 - 를 주면,
            # -4 + 1 + 2 + 1
            # = (4 + 1 + 2 + 1) - 2 * 4
            # = (sum_num) - 2 * sum(comb) 을 target 과 비교

            if sum_num + (-2) * sum(comb) == target:
                answer += 1
    return answer