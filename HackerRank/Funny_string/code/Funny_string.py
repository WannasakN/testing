def funnyString(s):
    a = []; b = []
    for i in range(1, len(s)):
        a.append(abs(ord(s[i]) - ord(s[i-1])))
        b.append(abs(ord(s[-i]) - ord(s[-i-1])))
    if a == b:
        return "Funny"
    return "Not Funny"
