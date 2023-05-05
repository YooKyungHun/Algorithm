from collections import Counter
from itertools import combinations

import sys
sys.setrecursionlimit(10**6)

N = int(input())
B = list(map(int, input().split()))
A = [0] * N
answer = -1

def func(B):
    global answer
    answer += 1

    # 종료조건
    if B == [0] * N:
        print(answer)
        exit()

    for i in range(len(B)):
        # B 에 홀수가 하나라도 있다면
        if B[i] % 2 != 0:
            # 홀수-1 을 집어넣고
            B.insert(i+1, B[i]-1)
            # 홀수를 빼버림
            B.pop(i)
            return func(B)

    # 홀수가 하나도 없다면
    B = [i // 2 for i in B]
    return func(B)

func(B)

#
#
# 16 15 7
# 16 14 7
# 16 14 6
# 8 7 3
# 8 6 3
# 8 6 2
# 4 3 1
# 4 2 1
# 2 1 1
# 2 0 1
# 2 0 0
# 1 0 0
# 0 0 0 => 12번
#
# 16 16 8
# 8 8 4
# 4 4 2
# 2 2 1
# 2 2 0
# 1 1 0
# 0 1 0
# 0 0 0 => 7번
#
# 16 8 4
# 8 4 2
# 4 2 1
# 4 2 0
# 2 1 0
# 2 0 0
# 1 0 0
# 0 0 0 => 7번
#
