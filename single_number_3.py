from collections import defaultdict

def number(nums):
    count = defaultdict(int)

    for i in nums:
        count[i] += 1
    return [k for k,v in count.items() if v == 1]

a = [1,2,1,3,2,5]

print(number(a))
