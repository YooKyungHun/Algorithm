import sys
input = sys.stdin.readline
from collections import defaultdict

N = int(input())

dic = defaultdict(int)
# print(dic)
for i in range(N):
    a, b = map(str, input().split('.'))
    dic[b] += 1
# defaultdict(<class 'int'>, {'txt\n': 3, 'spc\n': 2, 'icpc\n': 2, 'world\n': 1})


answer = []
for key in dic.keys():
    answer.append((key, dic[key]))
answer.sort(key = lambda x:x[0])
# [('icpc\n', 2), ('spc\n', 2), ('txt\n', 3), ('world\n', 1)]

for i in answer:
    print(f'{i[0][:-1]} {i[1]}')
