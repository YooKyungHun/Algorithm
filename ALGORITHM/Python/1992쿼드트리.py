n = int(input())

tree = [list(map(int, input())) for _ in range(n)]
# [1, 1, 1, 1, 0, 0, 0, 0], 
# [1, 1, 1, 1, 0, 0, 0, 0], 
# [0, 0, 0, 1, 1, 1, 0, 0], 
# [0, 0, 0, 1, 1, 1, 0, 0], 
# [1, 1, 1, 1, 0, 0, 0, 0], 
# [1, 1, 1, 1, 0, 0, 0, 0], 
# [1, 1, 1, 1, 0, 0, 1, 1], 
# [1, 1, 1, 1, 0, 0, 1, 1]]

def func(x, y, n):
  # 시작점: 제일 왼쪽 상단 값
  tmp = tree[x][y]

  for i in range(x, x+n):
    for j in range(y, y+n):
      # 현재 배열 단위를 하나의 값으로만 나타낼 수 없는 경우
      if tmp != tree[i][j]:
        print("(", end="")
        func(x,        y,        n//2)  # 좌상
        func(x,        y+(n//2), n//2)  # 우상
        func(x+(n//2), y,        n//2)  # 좌하
        func(x+(n//2), y+(n//2), n//2)  # 우하
        print(")", end="")
        return  # for 문이 아니라 func 를 끝내야하기 때문에 return

  # 현재 배열 단위를 하나의 값으로 나타낼 수 있는 경우
  if tmp == 0:
    print(0, end="")
  elif tmp == 1:
    print(1, end="")

func(0, 0, n)
