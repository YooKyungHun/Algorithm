# 일단 최소한의 개수 L 대신 특정개수 L 이라고 가정
def func(N, L):
  result = []

  while True:
    # 등차수열의 합
    # N = ( (L*start) + ((L-1)/2) + ((L-1)**2)/2 )

    start = int((2*N-L*L+L)*(2*L)**(-1))
    end = start + L - 1

    if start < 0:
      start = 0

    for i in range(start, end+1):
      result.append(i)

    # 리스트의 합 확인
    if (sum(result)) == N:
      print(*result)
      break
      
    else:
      # 최소한의 L 로 만족하는게 없어서 +1 해주고 다시 계산
      L += 1
      result = []
      if L > 100:
        print(-1)
        break
      
N, L = map(int, input().split())
func(N, L)