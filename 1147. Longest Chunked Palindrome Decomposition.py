def longestDecomposition(text):
    reversed_text = text[::-1]
    k = 0
    i = 1
    s = 0
    while i < len(text)+1:
        temp_t = reversed_text[s:i]
        if temp_t[::-1] == text[s:i]:
            # print(temp_t[::-1], text[s:i])
            # print(text[:i])
            k += 1
            s = i
        i += 1
    return k

if __name__ == "__main__":
    s = "ghiabcdefhelloadamhelloabcdefghi"
    s = "merchant"
    s = "antaprezatepzapreanta"
    s = "aaa"

    print(longestDecomposition(s))