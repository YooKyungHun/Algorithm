def solution(files):
    answer = []

    def split_func(file, idx):
        number_idx = []
        for i in range(len(file)):
            if 48 <= ord(file[i]) <= 57:  # isdigit() 사용가능
                number_idx.append(i)
            elif number_idx != []:
                break

        HEAD = file[0:number_idx[0]]
        NUMBER = file[number_idx[0]:number_idx[0] + len(number_idx)]
        TAIL = file[number_idx[0] + len(number_idx):]
        print((HEAD, NUMBER, TAIL, idx))
        return (HEAD,
                NUMBER,
                TAIL,
                idx)
        # ('img', '2', '.JPG', 5)

    lst = []

    for idx in range(len(files)):
        file = files[idx]
        lst.append(split_func(file, idx))
    '''
    lst = [['img', 12, '.png', 0, 'img', '12'], 
    ['img', 10, '.png', 1, 'img', '10'], 
    ['img', 2, '.png', 2, 'img', '02'], 
    ['img', 1, '.png', 3, 'img', '1'], 
    ['img', 1, '.GIF', 4, 'IMG', '01'], 
    ['img', 2, '.JPG', 5, 'img', '2']]
    '''

    lst.sort(key=lambda x: (x[0].lower(), int(x[1]), x[3]))
    '''
    lst = [('img', '1', '.png', 3), 
    ('IMG', '01', '.GIF', 4), 
    ('img', '02', '.png', 2), 
    ('img', '2', '.JPG', 5), 
    ('img', '10', '.png', 1), 
    ('img', '12', '.png', 0)]
    '''

    for HEAD, NUMBER, TAIL, idx in lst:
        answer.append(HEAD + NUMBER + TAIL)

    return answer