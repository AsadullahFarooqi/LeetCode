class Solution:
    def letterCasePermutation(self, S):
        S = S.lower()
        if not len(S) or S == S.upper():
            return [S]
        ans = set()
        for e in range(1, len(S)):
            for s in range(len(S)):
                if S[s:s+e].upper() != S[s:s+e].lower():
                    s = S[:s] + S[s:s+e] + S[s+e:]
                    ans.add(s)
                    ans.add(s.upper())
        return list(ans)

if __name__ == '__main__':
    s = "a1b2"
    s = "3z4"
    s = "c"
    s = "mQe"
    sol = Solution().letterCasePermutation(s)
    print(sol)

# ["MQe","mQE","mqe","Mqe","mqE","mQe","MQE"], 
# ['mqe', 'MQE', 'mqE', 'mQE', 'mQe', 'Mqe', 'MQe']
# ["mqe","mqE","mQe","mQE","Mqe","MqE","MQe","MQE"]