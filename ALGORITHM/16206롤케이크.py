N, M = map(int, input().split())
lst = list(map(int, input().split()))

# 10 의 배수들만
part1 = [i for i in lst if i % 10 == 0]
# 10 의 배수가 아닌 원소를 10 으로 나눈 몫만 담기
part2 = [i//10 for i in lst if i % 10 != 0]

# part1 에서 10 과 20 은 M 의 소모가 적으므로 먼저 계산하기 위해 정렬
part1.sort()
answer = 0
for i in part1:
    if i == 10:
        answer += 1
    elif i == 20 and M:
        answer += 2
        M -= 1
    elif i % 10 == 0 and M:
        # 1. M = 3 and i = 50 => answer 3개 추가, M 3번 사용
        # 2. M = 4 and i = 50 => answer 5개 추가, M 4번 사용
        # 3. M = 5 and i = 50 => answer 5개 추가, M 4번 사용
        if M+1 < i // 10:  # 1
            answer += M
            M -= M
        elif M+1 >= i // 10: # 2, 3
            answer += i // 10
            M -= i // 10 - 1

# part1 을 끝내고
# 남은 M = 8, part2 = [3x, 4x, 5x, 1x, 2x] 라면 => answer += 8
# 남은 M = 8, part2 = [1x, 2x] 라면 => answer += 3
# part2 를 10 으로 나눈 몫의 합과 M 을 비교하여 작은 수를 answer 에 더해주기
answer += min(M, sum(part2))

print(answer)

