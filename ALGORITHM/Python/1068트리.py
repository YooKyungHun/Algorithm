import sys

def DFS(target):
    tree[target] = -2
    for i in range(n):
        if tree[i] == target:  
            tree[i] = -2
            # tree 에서 target 을 부모노드로 가지는 노드를 제거하기 위해 DFS(재귀)
            DFS(i)


n = int(input()) 
tree = list(map(int, sys.stdin.readline().split()))  
target = int(input())
# n = 9
# tree = [-1, 0, 0, 2, 2, 4, 4, 6, 6]
# target = 4

# 리프노드의 판별
DFS(target)
cnt = n

# i = 0  1  2  3 | 4  5  6  7  8
# j = -1 0  0  2 | -2 -2 -2 -2 -2
# tree = 각 i 번 노드의 부모(tree)

# 조건 1. tree 에서 값이 -2 가 아니어야 하고
for i in range(n):
    if tree[i] == -2:
        cnt -= 1
    if tree[i] != -2:
        
        # 조건 2. 자식이 없는 노드이어야 함.
        # 리프노드 = 부모가 되어선 안됨.
        # 즉 -1, 0, 2 의 값을 가지면 안됨 -> 1번 3번 노드만 리프노드
        # i 반복문을 돌면서 j 값이 하나라도 있으면 리프노드에서 제외
        for j in tree:
            if j == i:
                cnt -= 1
                break
        
print(cnt)