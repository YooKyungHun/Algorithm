from datetime import datetime
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    today = datetime.strptime(today, '%Y.%m.%d')
    print(today)
    # 2022-05-19 00:00:00

    term_dict = {}
    for term in terms:
        Type, Month = map(str, term.split())
        term_dict[Type] = int(Month)
    # 	{'A': 6, 'B': 12, 'C': 3}

    idx = 1
    for privacy in privacies:
        start_date, agree_type = map(str, privacy.split())
        # 2021.05.02 A
        start_date = datetime.strptime(start_date, ('%Y.%m.%d'))
        tmp = start_date + relativedelta(months=int(term_dict[agree_type]))
        # 2021-11-02 00:00:00
        if tmp <= today:
            answer.append(idx)
        idx += 1

    return answer