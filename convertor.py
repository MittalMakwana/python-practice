def int_to_str(x):
    is_neg = 0
    if x < 0:
        is_neg = 1
        x = -x
    _temp = []
    while True:
        _temp.append(chr(ord('0') + x % 10 ) )
        x = x // 10
        if not x: break
    return ('-' if is_neg else '' ) + ''.join(_temp[::-1])


print(int_to_str(-123))


def str_to_int(x):

    is_neg = 0

    if x[0] == '-':
        is_neg = 1
        x = x[1:]

    _sum = lambda running_sum, c : running_sum * 10 + string.digits.index(c)

    from functools import reduce

    return reduce(_sum, x)


print(str_to_int('123'))
