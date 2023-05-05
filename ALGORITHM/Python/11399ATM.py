N = int(input())

lst = list(map(int, input().split()))

# person, time
arr = [(i, v) for i, v in enumerate(lst, 1)]
# [(1, 3), (2, 1), (3, 4), (4, 3), (5, 2)]

arr.sort(key = lambda x: x[1] )
# [(2, 1), (5, 2), (1, 3), (4, 3), (3, 4)]

answer = 0
for i in range(N):
    person, time = arr[i]
    answer += time * ( N - i )
print(answer)


# 1
# 1 2
# 1 2 3
# 1 2 3 3
# 1 2 3 3 4

# => 총 소요시간의 합계는?
#    1 분 5 번
#  + 2 분 4 번
#  + 3 분 3 번
#  + 3 분 2 번
#  + 4 분 1 번
# => time * 횟수
# =  time * (N - i)

