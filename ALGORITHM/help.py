# 이중배열
arr = [[1,2,3],[4,5,6],[7,8,9]]
# 1 2 3
# 4 5 6
# 7 8 9

# 전치
lst = list(map(list, zip(*lst)))
# 1 4 7
# 2 5 8
# 3 6 9

# 점대칭
lst = list(map(list, zip(*lst[::-1])))[::-1]
# 9 6 3
# 8 5 2
# 7 4 1

# 오른쪽 90도 회전
lst = list(map(list, zip(*lst[::-1])))
lst[i][j] = lst[N-1-j][i]
# 7 4 1
# 8 5 2
# 9 6 3

# 왼쪽 90도 회전
lst = list(map(list, zip(*lst)))[::-1]
# 3 6 9
# 2 5 8
# 1 4 7

# 시간 메모리 초과할 수 있으니 inf 보다 적당히 크고 작은 수를 넣을 것
min_sum = float('inf')
max_sum = float('-inf')

# 이중배열 테두리 두르기
arr = [list(map(int, input().split())) for _ in range(N)]
arr.insert(0, [0] * 100)
arr.append([0] * 100)

# Counter
from collections import Counter

tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
count = sorted(Counter(tangerine).items(), reverse=True, key=lambda x: x[1])
# [[3,2],[2,2],[5,2],[1,1],[4,1]]
count = Counter(tangerine).most_common()
# [[3,2],[2,2],[5,2],[1,1],[4,1]]
count = sorted(Counter(tangerine).items())
# [[1,1],[2,2],[3,2],[4,1],[5,2]]
count = sorted(Counter(tangerine).values())
# [1,1,2,2,2]
count = Counter(tangerine)
# {"1":1,"2":2,"3":2,"4":1,"5":2}