import sys
from collections import deque

TC = int(input())

for tc in range(TC):
  p = input()
  n = int(input())
  lst = sys.stdin.readline().rstrip()[1:-1].split(',')  
  # RDD 4 ['1', '2', '3', '4'] / (list)

  queue = deque(lst)

  flag = 0
  cnt_R = 0
  for i in range(len(p)):

    # 1) R 인 경우 count
    if p[i] == 'R':
      cnt_R += 1

    # 2) D 인경우 삭제하기
    elif p[i] == 'D':

      # 2-1) D 인데 빈 배열의 경우 
      if len(queue) == 0:
        flag = -1
        break
      # 2-2) D 인데 입력자체가 빈 배열로 들어온 경우
      elif n == 0:
        flag = -1
        break
      # 2-3) 빈 배열이 아닌 경우
      else:
        if cnt_R % 2 == 0: # 짝수번
          queue.popleft()
        else:              # 홀수번
          queue.pop()


  if flag == -1:
    print("error")
  elif cnt_R % 2 == 0:
    queue = list(map(str, queue))
    print('[', end='')
    for i in range(len(queue)):
      if i != len(queue)-1:
        print(queue[i], end=',')
      else:
        print(queue[i], end='')
    print(']')

    # print(list(map(str, queue)))
    
  elif cnt_R % 2 == 1:
    queue.reverse()
    queue = list(map(str, queue))
    print('[', end='')
    for i in range(len(queue)):
      if i != len(queue)-1:
        print(queue[i], end=',')
      else:
        print(queue[i], end='')
    print(']')

    # print(list(map(str, queue)))

