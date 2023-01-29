import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M, R = map(int, input().split())

arr = [[] for _ in range(N+1)]
arr2 = [[0] * N for _ in range(N+1)]
visited = [0] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
# arr = [[], [2, 4], [1, 3, 4], [2, 4], [1, 2, 3], []]

# for i in range(M):
#     a, b = map(int, input().split())
#     arr2[a][b] = 1
#     arr2[b][a] = 1
# arr2[a][b] = 1 이면 a 에서 b 를 갈 수 있다.
# [[0, 0, 0, 0, 0],
#  [0, 0, 1, 0, 1],
#  [0, 1, 0, 1, 1],
#  [0, 0, 1, 0, 1],
#  [0, 1, 1, 1, 0],
#  [0, 0, 0, 0, 0]]

cnt = 1
def DFS(R):
    global cnt
    arr[R].sort()

    for i in arr[R]:
        if visited[i] == 0:
            cnt += 1
            visited[i] = cnt
            DFS(i)

    # visited = [0, 1, 2, 3, 4, 0]

visited[R] = 1
DFS(R)
for i in range(1, N + 1):
    print(visited[i])




