
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 시계방향 90 도 회전
# arr = list(map(list, zip(*arr[::-1])))
# [7, 4, 1],
# [8, 5, 2],
# [9, 6, 3]

# 시계방향 270 도 회전
# arr = list(map(list, zip(*arr)))[::-1]
# [3, 6, 9],
# [2, 5, 8],
# [1, 4, 7]

arr = list(map(list, zip(arr)))[::-1]



print(arr)