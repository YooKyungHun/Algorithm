N, M =  map(int, input().split())  # 세로, 가로

arr = [list(map(int, input().split())) for _ in range(N)]
# [[1, 2, 3, 4, 5], 0
# [5, 4, 3, 2, 1], 
# [2, 3, 4, 5, 6],
# [6, 5, 4, 3, 2],
# [1, 2, 1, 2, 1]]

# I 모양(세로 4, 가로 1)
max_I = 0
for i in range(N-4+1):
    for j in range(M-1+1):
        sum_I=arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+3][j]
        if max_I<sum_I:
            max_I = sum_I

# L 모양(세로 3, 가로 2)
max_L = 0
for i in range(N-3+1):
    for j in range(M-2+1):
        sum_L=arr[i][j]+arr[i+1][j]+arr[i+2][j]+arr[i+2][j+1]
        if max_L<sum_L:
            max_L = sum_L

# 번개모양(세로 3, 가로 2)
max_X = 0
for i in range(N-3+1):
    for j in range(M-2+1):
        sum_X=arr[i][j]+arr[i+1][j]+arr[i+1][j+1]+arr[i+2][j+1]
        if max_X<sum_X:
            max_X = sum_X

print(max_I, max_L, max_X)