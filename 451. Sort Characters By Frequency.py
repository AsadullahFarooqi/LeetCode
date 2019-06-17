"""
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
    "Aabb"

Output:
    "bbAa"

Explanation:
    "bbaA" is also a valid answer, but "Aabb" is incorrect.
    Note that 'A' and 'a' are treated as two different characters.

Example 2:

Example 3:
"""
def frequencySort(s):

    a = [[0,i] for i in range(128)]
    for i in s:
        a[ord(i)][0] += 1

    a = sorted(a, reverse=True, key=lambda item: item[0])
    ans = ""
    for item in a:
        if item[0] == 0:
            break
        ans += item[0]*chr(item[1])

    return ans

if __name__ == '__main__':
    s = "Aabb"
    print(frequencySort(s))