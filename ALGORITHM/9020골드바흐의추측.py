import sys

# True: 소수
lst = [True] * 10000

for i in range(2, 100+1):
    if lst[i]:
        for j in range(i+i, 10000, i):
            lst[j] = False

TC = int(input())
for tc in range(1, TC+1):
    n = int(sys.stdin.readline())

    A = n // 2
    B = n // 2

    for i in range(10000):
        if lst[A] and lst[B]:
            print(A, B)
            break
        else:
            A -= 1
            B += 1


