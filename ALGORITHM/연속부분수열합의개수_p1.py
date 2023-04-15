# from itertools import

def solution(elements):
    answer = set()
    # 1 2 3 4 5 1 2 3 4
    N = len(elements)
    new_elements = elements + elements[0:N - 1]

    for i in range(1, N + 1):
        for j in range(N):
            tmp = sum(new_elements[0 + j: i + j])
            answer.add(tmp)

    return len(answer)