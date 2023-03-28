N, K = map(int, input().split())

lst = list(map(int, input().split()))

idx_lion = [i for i, v in enumerate(lst) if v == 1]
# [0, 4, 6, 9]


answer = len(lst)
for i in range(len(idx_lion) - K + 1):
    answer = min(idx_lion[i+K-1] - idx_lion[i], answer)

if len(idx_lion) < K:
    print(-1)
else:
    print(answer+1)
