def two_search(ARR, x):
    # Start from the top right
    row, col = 0, len(ARR[0]) - 1

    while row < len(ARR) and col >=0:
        print(row, col, ARR[row][col])
        if x == ARR[row][col] : return True
        if x < ARR[row][col]: col = col - 1
        if x > ARR[row][col]: row = row + 1
    return False



arr = [[-1,2,4,4,6],[1,5,5,9,18],[3,6,6,9,19],[3,6,8,10,24],[6,8,9,12,25],[18,20,22,34,40]]
for i in arr:
    print(i)
print(two_search(arr, 22))
