def twoCharacter(s):
    distinct_chars = set(s)
    max_length = 0
    for c1 in distinct_chars:
        for c2 in distinct_chars:
            if c1 != c2:
                filtered = [c for c in s if c == c1 or c == c2]
                if all(filtered[i] != filtered[i+1] for i in range(len(filtered)-1)):
                    max_length = max(max_length, len(filtered))
    return max_length
