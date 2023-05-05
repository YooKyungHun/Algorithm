N = int(input())
# 별 혹은 빈칸을 저장할 lst 초기화
# 모든 원소를 빈칸으로 초기화함
lst = [([' '] * N ) for _ in range(N)]
# N = 3 일때
# [[' ', ' ', ' '],
#  [' ', ' ', ' '],
#  [' ', ' ', ' ']]

def func(a, b, N):

    for i in range(3):
        for j in range(3):
            if N == 3:
                if i != 1 or j != 1:  # 이 조건의 반대는 i = j = 1
                    lst[a+i][b+j] = '*'

            else:
                if i == 1 and j == 1:
                    pass
                else:
                    func(a + N//3 * i, b + N//3 * j, N//3)

    return

func(0, 0, N)
for i in range(N):
    print(''.join(lst[i]))
