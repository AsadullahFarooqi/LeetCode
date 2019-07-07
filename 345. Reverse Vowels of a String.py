def reverseVowels(s):
    s = list(s)
    indxs = []
    vowels = []
    v = "aeiouAEIOU"
    for i in range(len(s)):
        if s[i] in v:
            indxs.append(i)
            vowels.append(s[i])
    
    vowels.reverse()
    for j in range(len(indxs)):
        s[indxs[j]] = vowels[j]
    return "".join(s)

if __name__ == '__main__':
    tests = {
        "hello": "holle",
        "leetcode": "leotcede",
    }

    for inp, out in tests.items():
        print(inp, "\n", "Solution Output: ", reverseVowels(inp), "\n", "Expected Output: ", out)
