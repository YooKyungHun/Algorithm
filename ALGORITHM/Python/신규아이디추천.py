import re


def func1(new_id):
    return new_id.lower()


def func2(func1_res):
    # allowed = ['a-z', 0-9, '-', '_', '.']

    allowed = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', '-', '_', '.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    func2_res = ''
    for i in func1_res:
        if i in allowed:
            func2_res = func2_res + i
    return func2_res


def func3(func2_res):
    while '..' in func2_res:
        func2_res = func2_res.replace('..', '.')

    func3_res = func2_res
    return func3_res


def func4(func3_res):
    if func3_res[0] == '.':
        func3_res = func3_res[1:]

    # length = len(func3_res)
    # if length != 0 and func3_res[-1] == '.':
    #     func3_res = func3_res[:length-1]

    func3_res = func3_res.rstrip('.')

    func4_res = func3_res
    return func4_res


def func5(func4_res):
    if func4_res == '':
        func4_res = 'a'
    func5_res = func4_res
    return func5_res


def func6(func5_res):
    if len(func5_res) >= 16:
        func5_res = func5_res[0:15]

        if func5_res[-1] == '.':
            func5_res = func5_res[0:14]

    func6_res = func5_res
    return func6_res


def func7(func6_res):
    if len(func6_res) <= 2:
        while len(func6_res) != 3:
            func6_res += func6_res[-1]

    func7_res = func6_res
    return func7_res


def solution(new_id):
    func1_res = func1(new_id)
    func2_res = func2(func1_res)
    func3_res = func3(func2_res)
    func4_res = func4(func3_res)
    func5_res = func5(func4_res)
    func6_res = func6(func5_res)
    func7_res = func7(func6_res)

    return func7_res