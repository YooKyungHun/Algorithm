N, K = map(int, input().split())
lst = list(map(int, input().split()))

if lst.count(1) < K:
    print(-1)
else:
    lion = [i for i, v in enumerate(lst) if v == 1]
    # [0, 4, 6, 9]

    print(min(lion[K - 1 + i] - lion[0 + i] + 1 for i in range(len(lion)-K+1)))
    # for i in range(len(lion) - K + 1):
    #     if min_idx > lion[K - 1 + i] - lion[0 + i]:
    #         min_idx = lion[K - 1 + i] - lion[0 + i]
    # print(min_idx + 1)

