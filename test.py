def allParenthesis(n, ps):
    '''
    ps init '('
    '''
    if n == 1:
        print('ps', ps)
        return ps
    else:
        temp_p = []
        for i in '()':
            for p in ps:
                temp_p.append(p + i)
        num = n - 1
        allp = temp_p
        return allParenthesis(num, allp)


if __name__ == '__main__':
    print(allParenthesis(3, ['(']))
