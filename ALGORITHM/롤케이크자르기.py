from collections import deque, Counter, defaultdict

def solution(topping):
    answer = 0

    cnter = Counter(topping)
    dic = defaultdict(int)
    # Counter({1: 4, 2: 2, 3: 1, 4: 1})
    # defaultdict(<class 'int'>, {})

    for top in topping:
        cnter[top] -= 1
        dic[top] += 1

        if cnter[top] == 0:
            del cnter[top]

        if len(cnter) == len(dic):
            answer += 1

    return answer


# Counter({1: 1, 2: 1, 3: 1, 4: 1}) 4
# Counter({1: 1, 3: 1, 4: 1, 2: 0}) 4
# Counter({1: 1, 4: 1, 2: 0, 3: 0}) 4
# Counter({4: 1, 1: 0, 2: 0, 3: 0}) 4
# Counter({1: 0, 2: 0, 3: 0, 4: 0}) 4