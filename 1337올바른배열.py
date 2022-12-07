import sys

N = int(input())
lst = []
for i in range(N):
  lst.append(int(input()))

lst.sort()
# [1, 5, 6, 7, 8, 9, 15]

# output
min_value = 5

cnt = 0
for i in lst:
  cnt = 0
  for j in range(1, 5):
    if (i+j) not in lst:
      cnt += 1
  
  if cnt < min_value:
    min_value = cnt

print(min_value)

    # if (i+2) in lst:
    #   if (i+3) in lst:
    #     if (i+4) in lst: