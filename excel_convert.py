def excel_to_int(_str):
  
    from functools import reduce
    _sum = lambda acc, val : acc * 26 + ( ord(val) - ord('A') + 1 ) # The formula inside return A:1, B:2, C:3 etc

    return reduce(_sum , _str, 0) # reduce(function, sequence, initial_value) setting the initial value as 0 so it take 0 + convert the first element

# This is yet left to complete
def int_to_excel(_int):
    _temp = []
    while True:
        _temp.append(chr( 64 + (_int % 26) + 1))

        _int //=26

        if _int == 0 : break
    return _temp


test_case = ["A","B","Y","Z","AB","ZY","zz","M", "BZ", "CCC"]

for _ in test_case:
    print("Excle col of {col} is {col_num} ".format(col = _, col_num = excel_to_int(_)))


print(int_to_excel(701))
