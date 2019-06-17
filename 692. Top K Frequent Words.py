"""
Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Input words contain only lowercase letters.
Follow up:
Try to solve it in O(n log k) time and O(n) extra space.
"""

def topKFrequent(words, k):
    """The algorithm works in the following steps
    1 - It makes an hash table to store the # of appearence 
    2 - Sorting the hash table keys by their values in reverse order
    3 - Returning the first k values
    
    Args:
        words (TYPE): Description
        k (TYPE): Description
    
    Returns:
        TYPE: Description
    """
    # step 1
        count_hash = {}
        for i in words:
            if i in count_hash:
                count_hash[i] += 1
                continue
            count_hash[i] = 1
        # step 2
        count_hash = sorted(count_hash, reverse=True, key=lambda item: count_hash[item])

        # steop 3
        return count_hash[:k]

if __name__ == '__main__':
    # n = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    n = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    print(topKFrequent(n, k))
