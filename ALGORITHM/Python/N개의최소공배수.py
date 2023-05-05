from math import gcd


def solution(arr):
    arr.sort()

    # 최소공배수
    LCM = arr[0]
    for i in range(1, len(arr)):
        GCD = gcd(LCM, arr[i])
        LCM = (LCM // GCD * arr[i] // GCD) * GCD

        return LCM

# 아이디어
# 5, 20 => GCD = 5 => [1, 4], 5 => 1 * 4 * 5 = 20
# 6, 21 => GCD = 3 => [2, 7], 3 => 2 * 7 * 3 = 42
# 4, 19 => GCD = 1 => [4, 19], 1 => 4 * 19 * 1 = 76

# 문제 TC
# 2 6 8 14
# => TCM = 2
# => TCM = 최소공배수(TCM, 6)
# => TCM = 최소공배수(TCM, 8)
# => TCM = 최소공배수(TCM, 14)

# 구현
# 2, 6 => LCM = 2 => LCM = (LCM // 2 * 6 // 2) * GCD = 6
# 6, 8 => LCM = 6 => LCM = (LCM // 2 * 8 // 2) * GCD = 24
