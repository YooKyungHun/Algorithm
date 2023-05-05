import math

TC = int(input())
for tc in range(TC):
    x, y = map(int, input().split())
    distance = y - x

    rt = math.sqrt(distance)  # 제곱근
    trk = math.trunc(rt)      # 제곱근의 정수부분

    if distance <= 3:
        print(distance)
    elif trk ** 2 == distance:
        print(trk*2 - 1)
    elif trk ** 2 < distance and distance <= trk ** 2 + trk:
        print(trk*2)
    else:
        print(trk*2 +1)



# 0 1  -> 1                 1
# 0 2  -> 1 1               2
# 0 3  -> 1 1 1             3
# 0 4  -> 1 2 1             3
# 0 5  -> 1 2 1 1           4
# 0 6  -> 1 2 2 1           4
# 0 7  -> 1 2 2 1 1         5
# 0 8  -> 1 2 2 2 1         5
# 0 9  -> 1 2 3 2 1         5
# 0 10 -> 1 2 2 2 2 1       6
# 0 11 ->                   6
# 0 12 ->                   6
# 0 13 ->                   7
# 0 14 ->                   7
# 0 15 ->                   7
# 0 16 -> 1 2 3 4 3 2 1     7