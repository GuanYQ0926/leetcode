def convert(s, numRows):
    len_s = len(s)
    if numRows == 1:
        return s
    if len_s <= numRows:
        return s
    else:
        outString = ''
        iter_size = numRows + (numRows - 2)
        iter_num = len_s / iter_size
        if len_s % iter_size != 0:
            iter_num += 1
        row_max = iter_num * (numRows - 1)
        s_log = []
        for i in range(len_s):
            group = i / iter_size
            pos = i % iter_size
            delta = pos - (numRows - 1)
            nrow = 0
            ncol = 0
            if delta <= 0:
                nrow = pos
            else:
                nrow = numRows - delta - 1
                ncol = delta
            indice = group * (numRows - 1) + ncol + row_max * nrow
            s_log.append(indice)
        outIndices = sorted(range(len(s_log)), key=lambda k: s_log[k])
        for i in outIndices:
            outString += s[i]
        return outString


if __name__ == '__main__':
    print(convert("ABC", 2))
