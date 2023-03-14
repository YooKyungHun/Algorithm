import sys
input = sys.stdin.readline

N = int(input())

root = [i for i in range(0, N+1)]

def find(x):
    if root[x] != x:
        root[x] = find(root[x])

    return root[x]

'''
1 3 5
1 1 3

find(5)    => root[5] = find(root[5]) = find(3)
 = root[5]    
 
find(3)    => root[3] = find(root[3]) = find(1)
 = root[3]
 
find(1)
 = root[1] = 1
'''


def union(a, b):
    A = find(a)
    B = find(b)

    if A > B:
        root[A] = B
    else:
        root[B] = A

for i in range(N-2):
    a, b = map(int, input().split())
    union(a, b)

# root = [0, 1, 1, 1, 4]

for i in range(1, N+1):
    if root[i] == i:
        print(i, end=' ')
