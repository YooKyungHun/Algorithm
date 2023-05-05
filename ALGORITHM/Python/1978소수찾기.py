import math
N = int(input())
lst = list(map(int, input().split()))
# [1, 3, 5, 7]
max_value = max(lst)

check = [True for _ in range(max_value+1)]
check[1] = False
for i in range(2, math.ceil((max_value+1)**0.5)):
    if check[i]:
        for j in range(i+i, max_value+1, i):
            check[j] = False

cnt = 0
for i in lst:
    if check[i]:
        cnt+=1
print(cnt)