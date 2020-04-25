def one(num):
    switch = { 
            0:'',
            1:'one',
            2:'two',
            3:'three',
            4:'four',
            5:'five',
            6:'six',
            7:'seven',
            8:'eight',
            9:'nine',
            10:'ten',
            11:'eleven',
            12:'twelve',
            13:'thirteen',
            14:'fourteen',
            15:'fifteen',
            16:'sixteen',
            17:'seventeen',
            18:'eighteen',
            19:'nineteen'
            }
    return switch.get(num)

def two(num):
    switch = {
            2:'twenty',
            3:'thrity',
            4:'fourty',
            5:'fifty',
            6:'sixty',
            7:'seventy',
            8:'eighty',
            9:'ninety'
            }
    return switch.get(num)


def get_two_digit(num):
    if num < 20:
        return convert(num)
    else:
        ten, unit = num //10 , num % 10
        return two(ten) + " " + one(unit)

def get_three_digit(num):
    hundred = num // 100
    two_digit = get_two_digit(num % 100)
    return one(hundred) + " hundred and " + two_digit if num > 99 else two_digit

def convert(num):
    result = ""
    billion = num // 1000000000
    million = (num - (billion * 1000000000)) // 1000000
    thousand = (num - (billion * 1000000000) - (million * 1000000)) // 1000
    hundred = num % 1000

    if billion:
        result += get_three_digit(billion) + ' Billion '

    if million:
        result += get_three_digit(million) + ' Million '

    if thousand:
        result += get_three_digit(thousand) + ' Thousand '

    if hundred:
        result += get_three_digit(hundred)

    return result




print(convert(124565))
