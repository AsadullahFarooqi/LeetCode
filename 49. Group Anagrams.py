def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    d = {}
    for i in strs:
        temp = "".join(sorted(i))
        if temp in d:
            d[temp].append(i)
            continue
        d[temp] = [i]
        
    return d.values()

if __name__ == '__main__':
    arr = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(arr))