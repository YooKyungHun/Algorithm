import sys
input = sys.stdin.readline

check = [True for _ in range(1000000 + 1)]

for i in range(2, 1001):
    if check[i]:
        for j in range(i+i, 1000001, i):
            check[j] = False
lst = [i for i in range(3, 1000001) if check[i] is True]

while True:
    n = int(input())
    if n == 0:
        break

    for i in lst:
        if check[n-i] is True:
            print(f'{n} = {i} + {n-i}')
            break
    if i == len(lst)-1:
        print("Goldbach's conjecture is wrong.")



