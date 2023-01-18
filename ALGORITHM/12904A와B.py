S = input()
T = input()

def func1(T):
    return T[0:len(T)-1]

def func2(T):
    return T[1:len(T)-1]

def func3(T):
    return T[0:len(T)-1][::-1]


while len(S) != len(T):
    # A 로 끝나는 경우
    if T[-1] == 'A':
        T = func1(T)

    # B 로 끝나고 맨 앞에도 A 인 경우
    elif T[-1] == 'B' and T[0] == 'A':
        T = func3(T)

    # B 로 끝나고 맨 앞에도 B 인 경우
    # + 둘 다 제거하기 위해 length 조건
    elif T[-1] == T[0] == 'B' and len(T) - len(S) >= 2:
        T = func2(T)

    # B 로 끝나고 맨 앞에도 B 인 경우
    # + 둘 다 제거하면 S > T 가 되어,
    # 맨 뒤 B 만 제거해야하는 경우
    elif T[-1] == T[0] == 'B' and len(T) - len(S) == 1:
        T = func3(T)  # BA, BAB

print(1 if S == T else 0)
