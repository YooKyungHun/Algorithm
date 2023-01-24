from collections import Counter
from itertools import combinations

import sys

input = sys.stdin.readline


def sol():
    n = int(input())
    ans = sum(map(int, input().split()))
    UP = list(map(int, input().split()))
    print(ans)

    UP.sort()
    for i in range(1, n):
        ans += UP[i] * i
    print(ans)


sol()