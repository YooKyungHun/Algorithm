import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, R = map(int, input().split())

arr = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
# print(arr) # [[], [4, 2], [1, 3, 4], [2, 4], [1, 2, 3], []]

visited = [0] * (N+1)

cnt = 1
def DFS(now):
    global cnt
    arr[now].sort()

    for i in arr[now]:
        if visited[i] == 0:
            cnt += 1
            visited[i] = cnt
            DFS(i)

visited[R] = 1
DFS(R)
for i in range(1, N+1):
    print(visited[i])