def solution(elements):
    n = len(elements)
    elements = elements * 2
    # [7, 9, 1, 1, 4, 7, 9, 1, 1, 4]

    result = set()
    for i in range(n):
        for j in range(n):
            result.add(sum(elements[i:i + j + 1]))  # ㄱ
            # result.add(sum(elements[j:j+i+1]))  # ㄴ
    return len(result)

# ㄱ 방법은 (1개~5개) * 5번 출력
# ㄴ 방법은 1개 5번, 2개 5번, ..., 5개 5번 출력

# 7
# 7 9
# 7 9 1
# 7 9 1 1
# 7 9 1 1 4
#   9
#   9 1
#   9 1 1
#   9 1 1 4
#   9 1 1 4 7
# ...
#         4
#         4 7
#         4 7 9
#         4 7 9 1
#         4 7 9 1 1