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
    """Summary
    The steps to solve the problem in this solution are
    1 - Make an array of 128 ASCII elements and ith element will have 
        2 elements of list [count, index]
    2 - Sort the ASCII array based on it's count or on it's 0th item of it's elements
    3 - Prepare the ans var
        iterate through ASCII array and convert the 2nd item of each element to
        it's character and then multiply it with it's count and append it
        to the answer.

    Time: O(128+s+128) => O(s)
    
    Args:
        s (string): input string to find the solution
    
    Returns:
        string: sorted string in decreasing order based on the frequency of characters
    """
    if len(s) == 0:
        return False
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