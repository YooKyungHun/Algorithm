import sys
sys.setrecursionlimit(10**9)
N = int(input())

length = 25
idx = 2
while True:
    if length >= N:
        break
    idx += 1
    length = length * 2 + (1 + 2 + idx)

# N 이 주어졌을 때 S(idx) 까지 해야 N 번째 문자를 구할 수 있음.
# dp = [3, 10, 25, ...]
# idx = [0, 1, 2]

# dp = [1, 4, 8]
# dp = dp + [8+3] + [x + (point * 2 + 1) for x in dp]
# S(0) = 1
# S(1) = 1 (4) 8 => 1->8: 7만큼
# S(2) = 1  4  8 (11) 16 19 23 => 1->16: 15 만큼
# S(3) = 1  4  8  11  16 19 23 (26) 32             1->32: 31만큼
#
dp = [1, 4, 8]
end = 8
point = 7
for i in range(2, idx+1):
    dp = dp + [end + 3] + [x + (point * 2 + 1) for x in dp]
    point = point * 2 + 1
    end = dp[-1]
print(dp)
print('m' if N in dp else 'o')
# [1, 4, 8, 11, 16, 19, 23, 26, 32, 35, 39, 42, 47, 50, 54]


