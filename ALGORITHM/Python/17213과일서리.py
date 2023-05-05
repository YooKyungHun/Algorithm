# 중복조합

from itertools import combinations_with_replacement

# 과일의 종류 수 N(1 ≤ N ≤ 10)
N = int(input())
# 훔치려 하는 과일의 개수 M(N ≤ M ≤ 30)
M = int(input())

cnt = 0
for cwr in combinations_with_replacement(range(1, N+1), M-N):
    cnt += 1

# 과일 
# A, B, C 총 3 개 중에 10개를 훔치는데, A, B, C 가 각각 최소한 1개씩 포함된다는 것은
# A, B, C 없어도 되고, 7개 중에 3개를 훔치는 것과 같음

# 반장선거
# 남자 3, 여자 2 에서 최소한 남자 1명을 포함하여 2명을 뽑는 것은
# 남자 2, 여자 2 에서 조건 없이 1명을 뽑는 경우의 수와 같음
print(cnt)   

