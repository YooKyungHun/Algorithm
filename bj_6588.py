import sys

def Goldbach():
    check = [True for _ in range(1000001)]
    
    for i in range(2, 1001):
        if check[i]:
            for j in range(i + i, 1000001, i):
                check[j] = False
ㅁ
    while True:
        n = in