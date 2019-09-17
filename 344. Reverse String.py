def reverseString(s):
        st= 0
        ed = len(s)-1
        while st < ed:
            e = s[st]
            s[st] = s[ed]
            s[ed] = e
            st += 1
            ed -= 1
        return
if __name__ == '__main__':
    s = ["h","e","l","l","o"]
    print(s)
    reverseString(s)
    print(s)