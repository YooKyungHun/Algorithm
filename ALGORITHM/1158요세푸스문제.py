from collections import deque

N, K = map(int, input().split())
lst = deque([i for i in range(1, N+1)])
# lst = [1, 2, 3, 4, 5, 6, 7]

print('<', end='')
# 맨 마지막 출력에서 ',' 없애기 위해
# 1개 남을때까지만 반복
while len(lst) > 1:
    # ex) K = 3 이라면
    # 앞에서 2번(K-1번) pop 하고 맨 뒤로 append 하면
    # 맨 앞에 있는 원소가 3(K)번째 숫자
    # [1, 2, 3, 4, 5, 6, 7]
    # [3, 4, 5, 6, 7, 1, 2]
    for _ in range(K-1):
        lst.append(lst.popleft())

    print(lst.popleft(), end=', ')

print(*lst, end='>')
