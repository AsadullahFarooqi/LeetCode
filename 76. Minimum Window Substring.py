import collections, pprint
def minWindow1(s, t):
    need = collections.Counter(t)            #hash table to store char frequency
    missing = len(t)                         #total number of chars we care
    start, end = 0, 0
    i = 0
    for j, char in enumerate(s, 1):          #index j from 1
        if need[char] > 0:
            missing -= 1
        need[char] -= 1
        if missing == 0:                     #match all chars
            while i < j and need[s[i]] < 0:  #remove chars to find the real start
                need[s[i]] += 1
                i += 1
            need[s[i]] += 1                  #make sure the first appearing char satisfies need[char]>0
            missing += 1                     #we missed this first char, so add missing by 1
            if end == 0 or j-i < end-start:  #update window
                start, end = i, j
            i += 1                           #update i to start+1 for next window
    return s[start:end]

def minWindow2(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    # Defaultdict is very useful in this problem, though i don't like to import modules
    target_count_dict = collections.defaultdict(int)
    for ch in t:
        target_count_dict[ch] += 1
    remain_missing = len(t)
    start_pos, end_pos = 0, float('inf')
    current_start = 0
    
    # Enumerate function makes current_end indexes from 1
    for current_end, ch in enumerate(s, 1):
        # Whenever we encounter a character, no matter ch in target or not, we minus 1 in count dictionary
        # But, only when ch is in target, we minus the length of remain_missing
        # When the remain_missing is 0, we find a potential solution.
        if target_count_dict[ch] > 0:
            remain_missing -= 1
        target_count_dict[ch] -= 1
        
        if remain_missing == 0:
            # Remove redundant character
            # Try to find the fist position in s that makes target_count_dict value equals 0
            # Which means we can't skip this character in s when returning answer
            while target_count_dict[s[current_start]] < 0:
                target_count_dict[s[current_start]] += 1
                current_start += 1
                pprint.pprint(target_count_dict)

            # if the found window s[current_start:current_end] is less then the
            # answer window s[end_pos:start_pos]
            if current_end - current_start < end_pos - start_pos:
                start_pos, end_pos = current_start, current_end
            
            # We need to add 1 to current_start, and the correspondence value in dictionary, is because
            # this is the first character of the potential answer. So, in future iteration, when we encounter this character,
            # We can remove this currently first character to try to find a shorter answer.
            target_count_dict[s[current_start]] += 1
            remain_missing += 1
            current_start += 1
    
    return s[start_pos:end_pos] if end_pos != float('inf') else ""


def minWindow3(s, t):
    need, missing = collections.Counter(t), len(t)
    i = I = J = 0
    for j, c in enumerate(s, 1):
        missing -= need[c] > 0
        need[c] -= 1
        if not missing:
            while need[s[i]] < 0: need[s[i]] += 1; i += 1
            if not J or j - i <= J - I: I, J = i, j
            need[s[i]] += 1; i += 1; missing += 1       # SPEEEEEEEED UP!
    return s[I : J]



def minWindow(s, t):
    need = collections.Counter(t)
    missing_chars = len(t)
    l,ans_l, ans_r = 0,0,0
    for r, character in enumerate(s, 1):
        if need[character] > 0:
            missing_chars -= 1
        need[character] -= 1
        if missing_chars == 0:
            while need[s[l]] < 0:
                need[s[l]] += 1
                l += 1
                
            if not ans_r or r-l < ans_r - ans_l:
                ans_l, ans_r = l,r
                
            need[s[l]] += 1
            missing_chars += 1
            l += 1
    return s[ans_l:ans_r]
    # need = collections.Counter(t)
    # missing = len(t)

    # # l => left pointer, l => right pointer
    # # a_s => answer start pointer
    # # a_e => answer end pointer
    # l, r, a_s, a_e = 0, 0, 0, 0

    # for r in range(len(s)):
    #     if need[s[r]] > 0:
    #         missing -= 1
    #     need[s[r]] -= 1
    #     r += 1
    #     if not missing:
    #         while l < r and need[s[l]] < 0:
    #             need[s[a_s]] += 1
    #             l += 1
    #         if a_e == 0 or r - l < a_e - a_s:
    #             a_s, a_e = l, r

    #             # if need[s[a_s]] > 0:
    #             #     missing += 1
    # return s[a_s:a_e]

    # need, missing = collections.Counter(t), len(t)
    # i = I = J = 0
    # for j, c in enumerate(s, 1):
    #     missing -= need[c] > 0
    #     need[c] -= 1
    #     if not missing:
    #         while i < j and need[s[i]] < 0:
    #             need[s[i]] += 1
    #             pprint.pprint(need)
    #             i += 1
    #         if not J or j - i <= J - I:
    #             I, J = i, j
    # return s[I:J]
    # def minWindow(self, s: str, t: str) -> str:


if __name__ == '__main__':
    S = "ADOBECODAEBANC"
    T = "AOC"
    # print(minWindow1(S, T))
    # print(minWindow2(S, T))
    # print(minWindow3(S, T))
    print(minWindow(S, T))
