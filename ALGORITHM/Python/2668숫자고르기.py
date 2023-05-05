
def DFS(v, i):
    visited[v] = True

    # 현재위치 v 에서 내가 갈곳 m 탐색
    for m in arr[v]:
        if visited[m] is False:
            DFS(m, i)
        # 원래 위치(i) 로 돌아왔다면
        elif visited[m] and m == i:
            result.append(m)

N = int(input())
arr = [[int(input())] for _ in range(N)]
arr.insert(0, [])
# [[], [3], [1], [1], [5], [5], [4], [6]]

result = []

for i in range(1, N+1):
    visited = [False] * (N+1)
    # 두번째 인자는 내가 다시 돌아올 수 있는 곳
    DFS(i, i)

print(len(result), *result, sep='\n')