from itertools import combinations

N = int(input())

# 체력 = [100, 50, 20, 13]
health = list(map(int, input().split()))
# 기쁨 = [20, 30, 40, 50]
pleasure = list(map(int, input().split()))

# [[체력, 기쁨], [체력, 기쁨], ... , [체력, 기쁨]]
lst = [[0, 0] for _ in range(N)]
for i in range(N):
    lst[i][0] = health[i]
    lst[i][1] = pleasure[i]
# [[100, 20], [50, 30], [20, 40], [13, 50]]

max_pleasure = 0
for i in range(1, N+1):  # i = 인사할 사람 수

    for comb in combinations(lst, i):
        comb = list(comb)
        health_cb = 0
        pleasure_cb = 0

        for j in range(len(comb)):  # len(comb) = i 랑 같음
            health_cb += comb[j][0]
            pleasure_cb += comb[j][1]

        # 체력소모는 100보다 작아야 하고, 기쁨은 최신화
        if health_cb < 100 and pleasure_cb > max_pleasure:
            max_pleasure = pleasure_cb
            
print(max_pleasure)
