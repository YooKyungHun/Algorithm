from collections import deque
# deque는 원소를 앞뒤로 삽입, 제거가 용이한 대신에
# 특정 인덱스에 접근하는데에는 비효율적입니다.

N = int(input())
lst = list(map(int, input().split()))
NGE = [-1] * N
stack = []

for i in range(0, N):
    # 스택이 비어있는 경우(맨 처음) 인덱스를 삽입
    if not stack:
        stack.append(i)

    # 스택이 비어있지 않은 경우
    else:
        # 오큰수가 없으면 인덱스를 삽입
        if lst[stack[-1]] >= lst[i]:
            stack.append(i)

        # 오큰수가 나타나면
        else:
            while stack:
                # 현재 lst[i] 보다 작은 값들만 pop 하고
                # 현재 lst[i] 보다 큰 값들은
                # 다음 오큰수가 나타날때까지 그대로 둠
                if lst[stack[-1]] < lst[i]:
                    # 삽입했던 인덱스를 pop 하면서
                    # 인덱스 활용하여 NGE 에 오큰수 할당
                    NGE[stack.pop()] = lst[i]
                else:
                    break
            stack.append(i)

print(*NGE)


#     9    5    4    8    10
# -------------stack--------
#     9
#     9    5
#     9    5    4
#     9    8    8    8       -> NGE[1] = 8, NGE[2] = 8
#     10   10   10   10   -1 -> NGE[0] = 10, NGE[3] = 10, NGE[4] = -1(기본값)