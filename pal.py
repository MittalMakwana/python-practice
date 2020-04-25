import collections
def can_pal(st):
    char_count = collections.defaultdict(int)

    for c in st:
        if char_count.get(c):
            char_count[c] +=1
        else:
            char_count[c] = 1
    odd_count = 0
    for k,v in char_count.items():
        if v % 2 == 1:
            odd_count += 1
    print(char_count,odd_count)
    return odd_count <= 1



print(can_pal('geeksogeeks'))
print(can_pal('geeksforgeeks'))
