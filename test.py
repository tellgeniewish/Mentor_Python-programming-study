def initials(s):
    words = s.split()
    result = ''
    for w in words:
        result += w[0].upper()
    return result

s = input()
print(initials(s))