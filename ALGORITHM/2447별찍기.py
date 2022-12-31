N = int(input())
# 별 혹은 빈칸을 저장할 lst 초기화
# 모든 원소를 빈칸으로 초기화함
lst = [([' '] * N ) for _ in range(N)]
# N = 3 일때
# [[' ', ' ', ' '],
#  [' ', ' ', ' '],
#  [' ', ' ', ' ']]

def func(N, row, col):
    for i in range(3):
        for j in range(3):

            # 가장 낮은 단계
            if N == 3:
                if i == 1 and j == 1:
                    lst[row + i][col + j] = ' '
                else:
                    lst[row + i][col + j] = '*'

            else:
                # 3 * 3 기준으로 (1, 1)의 경우 빈칸(초기값)으로 그대로 둠(재귀를 실행하지 않음)
                # 초기값을 0 이 아닌 빈칸으로 설정한 이유임.
                if i == 1 and j == 1:
                    pass
                # 나머지는 8곳(9-1) 에 대해서만 재귀
                else: # i != 1 or j != 1:
                    func(N // 3, row + i * (N // 3), col + j * (N // 3))
                    # func(3, 0, 0) (3, 0, 1) (3, 0, 2)
                    #     (3, 1, 0) ( ----- ) (3, 1, 2)
                    #     (3, 2, 0) (3, 2, 1) (3, 2, 2)
    # return

func(N, 0, 0)

for i in range(N):
    print(''.join(lst[i]))