N = int(input())

students = [input() for _ in range(N)]
# students = ['1212345', '1212356', '0033445']
length = len(students[0])
# length = 7

# 구하고자 하는 최소 K 값
for k in range(1, length+1):
    numbers = []

    for student in students:
        number = student[length-k:]
        # 중복 O
        if number in numbers:
            break
        # 중복 X
        else:
            numbers.append(number)

    if len(numbers) == N:
        print(k)
        break
