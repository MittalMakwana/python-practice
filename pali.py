def is_pali(s):
    i, j = 0, len(s) - 1

    while i < j:
        
        while not s[i].isalnum():
            i += 1

        while not s[j].isalnum():
            j -= 1

        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1
    return True


a = "!!A man, a plan, a canal: Panama"
b = "race a car"

print(is_pali(a))
print(is_pali(b))
