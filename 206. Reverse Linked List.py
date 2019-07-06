def reverseList(head):
    if head == None or head.next == None:
        return head

    iterator = head.next
    curr = head
    prev = None
    while iterator != None:
        curr.next = prev
        prev = curr
        curr = iterator
        iterator = iterator.next
    curr.next = prev
    prev = curr
    return prev
