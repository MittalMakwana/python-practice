def rel_sort(arr1, arr2):
    d = {i : 0 for i in arr2}
    r, t = [] , []
    for i in arr1:
        if i in d:
            d[i] += 1
        else:
            t.append(i)

    t.sort()
    for j in arr2:
        r.extend([j]*d[j])

    return r + t


arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]

print(rel_sort(arr1, arr2))
