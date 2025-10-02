if __name__ == '__main__':
    line = input('Enter a string: ') + '$'

    res = []
    start_idx = 0

    for idx in range(len(line)):
        if line[idx] != line[idx-1]:
            ln = idx - start_idx
            res.append((-ln, line[idx-1]))
            start_idx = idx

    res.sort()
    for idx,(freq, char) in enumerate(res):
        freq = -freq
        if freq == 1:
            res[idx] = char
        else:
            res[idx] = '{}{}'.format(freq, char)

    print('_'.join(res))
