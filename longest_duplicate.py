def find_longest_dup(s):
    hashset = set()

    result = []

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if s[i:j] not in hashset:
                hashset.add(s[i:j])
            else:
                result.append(s[i:j])
    return max(result, key=len) if result else ""


print(find_longest_dup("tesc"))
