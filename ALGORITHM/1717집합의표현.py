# lst = [1]
# lstt = [2]
# t = set(lst)
# tt = set(lstt)
# # print(set.union(t, tt))

# tst = [True, True, False, False]
# ttst = [True, False, True, False]
#
# for i in range(4):
#     print(tst[i] or ttst[i])


N, M = map(int, input().split())
arr = [[False] * (N+1) for _ in range(N+1)]

for i in range(N+1):
    arr[i][i] = True

for i in range(M):
    boolean, a, b = map(int, input().split())

    for j in range(M):
        if boolean == 0:
            arr[a][j] = (arr[a][j] or arr[b][j])
            arr[b][j] = (arr[a][j] or arr[b][j])
        else:
            pass
    if boolean == 1:
        if arr[a][b] is True:
            print('YES')
        else:
            print('NO')

print(arr)


#
# 3 4
# 0 0 1
# 0 2 3
# 0 1 2
# 1 0 3