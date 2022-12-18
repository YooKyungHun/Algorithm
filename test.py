from itertools import combinations



N = 5
lst = [1, 2, 3, 4, 5, 0]
for i in range(N):
    comb = list(combinations(lst, i+1))
    print(comb)

print((1, 2, 3)[0])


lst.sort()
print(lst)