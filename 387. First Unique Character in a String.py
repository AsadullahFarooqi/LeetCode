def firstUniqChar(s):
    """in this solution i make a hash map and since the hash map
    will hold the key value pairs in the same order in which they
    presented in the string. So after the first loop when the hash 
    map is ready i'll just iterate through the hash map to get the
    first element which count/val is 1 and return it
    otherwise the function will return -1 
    
    Args:
        s (string): string to find first non repeating character
    
    Returns:
        int: index of the first non repeating character index or -1 if not exist
    """
    d = {}
    for i in s:
        if i in d: d[i] += 1
        else: d[i] = 1
    for k,v in d.items():
        if v == 1:
            return s.index(k)
    return -1

if __name__ == '__main__':
    s = "leetcode"
    firstUniqChar(s)