"""

Given a non-empty array of integers, return the k most frequent elements.

Example 1:
    Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

Example 2:
    Input: nums = [1], k = 1
    Output: [1]

Note:
    You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
    Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""


def topKFrequent(nums, k):
    """The algorithm works in the following steps
    1 - It makes an hash table to store the # of appearence 
    2 - Sorting the hash table keys by their values in reverse order
    3 - Returning the first k values
    
    Args:
        nums (TYPE): Description
        k (TYPE): Description
    
    Returns:
        TYPE: Description
    """
    # step 1
    count_hash = {}
    for i in nums:
        if i in count_hash:
            count_hash[i] += 1
            continue
        count_hash[i] = 1
    # step 2
    count_hash = sorted(count_hash, reverse=True, key=lambda item: count_hash[item])

    # steop 3
    return count_hash[:k]

if __name__ == '__main__':
    # n = [1,1,1,2,2,3]?
    # n = [1]
    n = [3,0,1,0]
    k = 1
    print(topKFrequent(n, k))
