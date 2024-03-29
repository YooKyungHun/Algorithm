'''
멀리뛰기_s1 은 메모이제이션 => 성공
멀리뛰기_s2 은 재귀 => 시간초과
'''

def func(n):
    if n == 1: return 1
    if n == 2: return 2

    return func(n - 1) % 1234567 + func(n - 2) % 1234567


def solution(n):
    tmp = func(n)

    return tmp % 1234567

# 2 칸
# 1 + 1
# 2

# 3 칸
# 1 + 1 + 1
# 1 + 2
# 2 + 1

# 4 칸
# 1 + 1 + 1 + 1
# 1 + 1 + 2
# 1 + 2 + 1
# 2 + 1 + 1
# 2 + 2

# 5 칸
# 1 + 1 + 1 + 1 + 1
# 1 + 1 + 2 + 1
# 1 + 2 + 1 + 1
# 2 + 1 + 1 + 1
# 2 + 2 + 1

# 1 + 1 + 1 + 2
# 1 + 2 + 2
# 2 + 1 + 2