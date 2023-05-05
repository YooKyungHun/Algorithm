def solution(board):
    answer = 1234

    N, M = len(board), len(board[0])

    for i in range(1, N):
        for j in range(1, M):
            if board[i][j]:
                board[i][j] = min(board[i - 1][j], board[i][j - 1], board[i - 1][j - 1]) + 1

    # [[0, 1, 1, 1],
    # [1, 1, 2, 2],
    # [1, 2, 2, 3],
    # [0, 0, 1, 0]]
    # board[i][j] = board[0][0] 부터 가능한 가장 큰 정사각형의 길이(0 인곳 제외)

    return max(map(max, board)) ** 2