import sys
from itertools import combinations

n = int(sys.stdin.readline())

lst = []

# 존재하지 않는 N 번째 감소하는 수
# -> 가장 큰 N 번째 감소하는 수는 9876543210
# -> 숫자가 최대한 1개씩만 들어갈 수 있음
# -> 조합으로 접근

# i = 조합하는 숫자의 개수(1개부터 10개까지)
for i in range(1, 11):
    for comb in combinations(range(0, 10), i):
        comb = list(comb)
        comb.sort(reverse=True)
        # [[0], [1], [2], [3], [4], [5], [6], [7], [8], [9],
        #  [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], 
        #  [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], 
        #  [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2],
       
        # 리스트 탈출작업
        lst.append(int("".join(map(str, comb))))

# 20 다음 30이 아니라 21이 와야함
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 
# 10, 20, 30, 40, 50, 60, 70
lst.sort()

if len(lst) <= n:
    print(-1)
else: 
    print(lst[n])


