from itertools import combinations



# N = 5
# lst = [1, 2, 3, 4, 5, 0]
# for i in range(N):
#     comb = list(combinations(lst, i+1))
#     print(comb)

# print((1, 2, 3)[0])


# lst.sort()
# print(lst)

s1 = set([1, 2, 3, 4, 5])
s3 = {1, 2, 3, 4, 5}

s1.add(5)
s3.add(5)
print(s1,s3)

# s1 = str(1234567)
# print(s1[7-1:])

print(len(s1))

for i in range(1, 11):
    print(i)

    if i == 5:
        continue


students = [input() for _ in range(3)]
print(students)