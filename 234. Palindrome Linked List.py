class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def isPalindrome(head):
    num = ""
    while head:
        num += str(head.val)
        head = head.next
    
    return num == num[::-1]

if __name__ == '__main__':
    print(isPalindrome(head))