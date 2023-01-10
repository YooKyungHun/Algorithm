N = int(input())

idx = 0
flag = 1
while True:
    if (N - 3 * idx) % 5 == 0:
        break
    if 3 * idx > N:
        flag = 0
        break
    idx += 1

if flag == 0:
    print(-1)
else:
    print(idx + (N-3*idx) // 5)