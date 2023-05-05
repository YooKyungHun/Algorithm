import sys
input = sys.stdin.readline

N, M = map(int, input().split())
K = int(input())
arr = [list(map(str, input())) for _ in range(N)]

# arrJ[i][j] = a,b,c,d 기준 (1, 1) ~ (i, j) 내에 J 가 몇 번 있는지 count 한 값
arrJ, arrO, arrI = [[0] * (M+1) for _ in range(N+1)], [[0] * (M+1) for _ in range(N+1)], [[0] * (M+1) for _ in range(N+1)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'J': arrJ[i+1][j+1] = 1
        if arr[i][j] == 'O': arrO[i+1][j+1] = 1
        if arr[i][j] == 'I': arrI[i+1][j+1] = 1

# arrJ = [[0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 0, 0, 1, 0, 0, 1],
#         [0, 0, 0, 1, 0, 0, 1, 0],
#         [0, 1, 0, 0, 1, 0, 0, 0],
#         [0, 0, 0, 1, 1, 0, 1, 0]]

for i in range(1, N+1):
    for j in range(1, M+1):
        arrJ[i][j] += arrJ[i][j-1] + arrJ[i-1][j] - arrJ[i-1][j-1]
        arrO[i][j] += arrO[i][j-1] + arrO[i-1][j] - arrO[i-1][j-1]
        arrI[i][j] += arrI[i][j-1] + arrI[i-1][j] - arrI[i-1][j-1]

# arrJ = [[0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 1, 1, 1, 2, 2, 2, 3],
#         [0, 1, 1, 2, 3, 3, 4, 5],
#         [0, 2, 2, 3, 5, 5, 6, 7],
#         [0, 2, 2, 4, 7, 7, 9, 10]]
# ex) a, b = 2, 2
#     c, d = 3, 6 이면
#     cntJ = arrJ[3][6] - arr[1][6] - arr[3][1] + arr[1][1]
# 면적으로 생각하면 쉬움

for k in range(K):
    cntJ, cntO, cntI = 0, 0, 0

    a, b, c, d = map(int, input().split())

    cntJ = arrJ[c][d] - arrJ[a-1][d] - arrJ[c][b-1] + arrJ[a-1][b-1]
    cntO = arrO[c][d] - arrO[a-1][d] - arrO[c][b-1] + arrO[a-1][b-1]
    cntI = arrI[c][d] - arrI[a-1][d] - arrI[c][b-1] + arrI[a-1][b-1]

    print(cntJ, cntO, cntI)
