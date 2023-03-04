from collections import deque



def DFS(now, summit, n, arr, other_gate, visited, tmp):

    if now == summit:
        print(tmp)
        return

    for next in range(1, n + 1):
        if arr[now][next] != 0 and next not in other_gate and visited[next] == 0:
            visited[next] = 1
            tmp.append(next)
            DFS(next, summit, n, arr, other_gate, visited, tmp)
            visited[next] = 0
            tmp.remove(next)


def solution(n, paths, gates, summits):
    answer = []

    arr = [[0] * (n + 1) for _ in range(n + 1)]
    for i, j, w in paths:
        arr[i][j] = w
        arr[j][i] = w
    #  [[0, 0, 0, 0, 0, 0, 0],
    # G [0, 0, 3, 0, 0, 0, 0],
    #   [0, 3, 0, 5, 2, 4, 0],
    # G [0, 0, 5, 0, 4, 0, 0],
    #   [0, 0, 2, 4, 0, 3, 1],
    # S [0, 0, 4, 0, 3, 0, 1],
    #   [0, 0, 0, 0, 1, 1, 0]]

    for gate in gates:
        for summit in summits:
            other_gate = [i for i in gates if i != gate]
            visited = [0] * (n + 1)
            visited[gate] = 1
            tmp = []
            tmp.append(gate)
            print(DFS(gate, summit, n, arr, other_gate, visited, tmp))

    return answer


solution(6, [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]], [1, 3], [5] )
# solution(7, [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]], [1], [2, 3, 4])