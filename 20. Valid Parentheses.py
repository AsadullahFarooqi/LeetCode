class Solution(object):
    def isValid(self, s):
        stack_ = []
        for i in s:
            if not i in "({[" or not i in ")}]": continue
            if i in "({[":
                stack_.append(i)
                continue
            elif not len(stack_):
                return False
            elif i == ")" and stack_.pop() != "(":
                return False
            elif i == "}" and stack_.pop() != "{":
                return False
            elif i == "]" and stack_.pop() != "[":
                return False

        return not len(stack_)


if __name__ == '__main__':
    s = "()"
    s = "()[]{}"
    s = "(]"
    s = "([)]"
    s = "{[]}"
    s = "(a[0]+b[2c[6]] {24 + 53}"
    sol = Solution().isValid(s)
    print(sol)