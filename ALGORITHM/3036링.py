N = int(input())
lst = list(map(int, input().split()))
tmp = lst[0]

def func(a, b):
    m = min(a, b)
    for i in range(m, 0, -1):  # m 부터 1까지
        if a % i == 0 and b % i == 0:
            a, b = a // i, b // i
            break
    return (a, b)

for i in range(1, N):
    a, b = func(tmp, lst[i])
    print(f'{a}/{b}')