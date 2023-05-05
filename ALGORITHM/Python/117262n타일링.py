# 메모이제이션

N = int(input())

lst = [0] * 1001
lst[0], lst[1], lst[2] = 0, 1, 2
# lst = [0, 1, 2, 0, 0 .... 0, 0]

def func(N):
    # 이미 있는 값의 경우
    if lst[N] > 0:
        return lst[N]

    else:
        lst[N] = func(N-1) + func(N-2)
        return lst[N]

print(func(N)%10007)










# def func(N):
#     if N == 1:
#         return 1
    
#     if N == 2:
#         return 2

#     if N >= 3:
#         return func(N-1) + func(N-2)
