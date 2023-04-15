def solution(number, k):
    stack = []
    for num in number:
        # 조건1) stack 이 있을 때 pop
        # 조건2) 현재 num 보다 크거나 같은 수가 나올때까지, 작은 수를 pop
        # 조건3) k번 빼내면 되니까 k > 0
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)

    # 만약 k 가 남았다면 while 문을 적게 돌린 셈이고, 자리 수가 더 크게 들어가 있음.
    test = "abcde"
    print(test[:-1])
    # if k != 0:
    #     stack = stack[:-k]
    return ''.join(stack)
