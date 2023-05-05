import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# arr = [[arr[0][0]] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            pass
        elif i == 0 and j != 0:
            arr[i][j] = arr[i][j] + arr[i][j-1]
        elif i != 0 and j == 0:
            arr[i][j] = arr[i][j] + arr[i-1][j]
        else:
            arr[i][j] = arr[i][j] - arr[i-1][j-1] + arr[i][j-1] + arr[i-1][j]

arr.insert(0, [0] * N)
for i in arr:
    i.insert(0, 0)
# [[0, 0, 0, 0, 0],
#  [0, 1, 3, 6, 10],
#  [0, 3, 8, 15, 24],
#  [0, 6, 15, 27, 42],
#  [0, 10, 24, 42, 64]]

# 면적으로 생각하기
'''
                 0, 0, 0, 0, 0         0, 0, 0, 0, 0      0, 0,     0, 0   
8, 15, 24    =   0, 1, 3, 6, 10      - 0, 1, 3, 6, 10   - 0, 1,  +  0, 1
15, 27, 42       0, 3, 8, 15, 24                          0, 3,
                 0, 6, 15, 27, 42                         0, 6,

'''
for i in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(arr[x2][y2] - arr[x1 - 1][y2] - arr[x2][y1 - 1] + arr[x1 - 1][y1 - 1])