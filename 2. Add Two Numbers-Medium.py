# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


def pop_dig(l1, l2):
    ans = 0
    for i in (l1, l2):
        num = ""
        while i:
            num = num + str(i.val)
            i = i.next
        ans += int(num[::-1])
    ans = str(ans)[::-1]

    temp1 = ListNode(int(ans[0]))
    temp2 = temp1
    for i in ans[1:]:
        a = ListNode(int(i))
        temp2.next = a
        temp2 = a

    return temp1


if __name__ == '__main__':

    for i in range(2):
        number_of_sections = int(input())
        wall = input().strip()
        print("Case #{}: {}".format(i, solution(number_of_sections, wall)))
        # check out .format's specification for more formatting options

    temp1 = ListNode(int(s[-1]))
    temp2 = temp1

    l = ListNode(2)
    n = ListNode(4)
    m = ListNode(3)
    l.next = n
    n.next = m

    a = ListNode(5)
    b = ListNode(6)
    c = ListNode(4)
    a.next = b
    b.next = c

    p = pop_dig(l, a)
    while p:
        print(p.val)
        p = p.next
