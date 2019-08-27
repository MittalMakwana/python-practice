def decoding(_str):
    count = 0
    result = []
    for _ in _str:
        if _.isdigit():
            count = count * 10 + int(_)
        else:
            result.append(count*_)
            count = 0

    return ''.join(result)

def encoding(_str):

    result = []
    count = 1
    for i in range(1, len(_str) + 1):
        if i == len(_str) or _str[i] != _str[i -1]:
            result.append(str(count) + _str[i-1])
            count = 1
        else:
            count += 1
    return ''.join(result)

print(decoding('4a3b2c2a'))
print(encoding('aaaaabbbbcccaa'))
