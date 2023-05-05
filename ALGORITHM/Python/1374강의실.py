import sys
input = sys.stdin.readline
from heapq import heappop, heappush

n = int(input())

heap = []
count = 0
for _ in range(n):
    num, start, end = map(int, input().split())
    heappush(heap, [start,end,num])

classroom = []
start, end, num = heappop(heap)
heappush(classroom, end)
while heap:
    start, end, num = heappop(heap)
    if classroom[0] <= start:
        heappop(classroom)
    heappush(classroom, end)
print(len(classroom))

# 3  7  2  6  6
# 8 13 14 20 27
#  9 11

# start 는 무조건 7보다 크거나 같음
# start 가 8보다 작다면, 겹침
# start 가 8과 같다면, 안겹침 => 8 에 끝나고, 8 에 시작하기 가능
# start 가 8보다 크다면, 안겹침
#
# ((((( ) ) ) ) )
#        (   )
# (((((   ) ))) )
# 8 11 13 14 20 27
#   11 13 14 20 27
#
# 2 3 4 5 6 7 8 9 10 11 12 13 14
#   3 4 5 6 7 8
#         6 7 8 9 10 11 12 13 14 15 16 17 ... 20
#         6 7 8 9 10 11 12 13 14 15 16 17 ... 20 ... 27
#           7 8 9 10 11 12 13

#           7 8 9 10 11 => 겹침   11 넣고
#             8 9 10 11 => 안겹침 8 빼고 11 넣고
#               9 10 11 => 안겹침 8 빼고 11 넣고
#-------------------------------------------------
# 인풋: 12-22, 15-21, 16-19, 19-25
# start = [12, 15, 16, 19]
# end = [19, 21, 22, 25]
# 변경: 12-19, 15-21, 16-22, 19-25
#
# 12 13 14 15 16 17 18 19
#          15 16 17 18 19 20 21
#             16 17 18 19 20 21 22
#                      19 20 21 22 23 24 25
#
# 12 13 14 15 16 17 18 19 20 21 22
#          15 16 17 18 19 20 21
#             16 17 18 19
#                      19 20 21 22 23 24 25