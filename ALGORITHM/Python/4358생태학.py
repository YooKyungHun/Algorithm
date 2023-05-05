from collections import defaultdict
import sys

dic = defaultdict(int)
length = 0
# sys.stdin.readline은 EOFError를 발생시키지 않고,
# 입력의 끝에 도달하면 빈 문자열을 반환합니다.
# if not tmp는 tmp 가 bool 값 False를 가지고 있기 때문에 만족되는 문장이 아니라,
# str을 조건문에 사용했을 때 참/거짓으로 판단되는 기준이
# 그 문자열이 빈 문자열이면 False, 그 외에는 True로 평가되는 것이기 때문입니다.
# 따라서 이 경우에는 그냥 input이 아니라
# sys.stdin.readline이 반드시 사용되어야만 합니다.
# 그냥 input은 EOFError를 발생시키 때문에 이 방법을 쓸 수 없습니다.

while True:
    tmp = sys.stdin.readline().strip()
    if not tmp:
        break

    dic[tmp] += 1
    length += 1

dic_sort = sorted(dic.items())
# lst.sort()
for name, num in dic_sort:
    print(f'{name} {100*dic[name] / length:.4f}')

# print(dic_sort)
# dic_sort : [('Ash', 4), ('Aspen', 1), ('Basswood', 1), ('Beech', 1),