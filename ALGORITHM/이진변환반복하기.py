def solution(s):
    answer = []
    cnt_zero = 0
    cnt_bin_change = 0

    while s != '1':
        cnt_zero += s.count("0")
        cnt_one = s.count("1")

        s = bin(cnt_one)
        s = str(s[2:])
        cnt_bin_change += 1

    return cnt_bin_change, cnt_zero