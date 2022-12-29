A, B = map(str, input().split())

def func(A, B):
    cnt = 0
    for i in range(len(A)):
        if A[i] != B[i]:
            cnt += 1
    return cnt

lst = []

tmp = 0
for i in range(len(B)-len(A)+1):
    cnt = func(A, B[0+tmp : len(A)+tmp])
    lst.append(cnt)
    tmp += 1

print(min(lst))

# abc -> 2
#  abc -> 1
#   abc -> 3
#    abc -> 1
#     abc -> 1
# aababbc -> min(lst) = 1