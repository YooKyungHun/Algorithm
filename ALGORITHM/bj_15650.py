import sys

def func(N, M):
  
  for i in range(1, N):
    tmp = []
    tmp.append(i)
    for j in range(i+1, N+1):
      if len(tmp)<M:
        tmp.append(j)
      if len(tmp) == M:
        print(*tmp)
        tmp.pop()

N, M = map(int, input().split())

func(N, M)
