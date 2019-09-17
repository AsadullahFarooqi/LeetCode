def reverseBetween(head, m, n):
    if head == None or head.next == None:
        return head

    iterator = head.next
    curr = head
    prev = None
    indx = 1
    while indx <= n:
        if indx < m:
            indx += 1
            prev = currs
            iterator = iterator.next
            curr = iterator
            continue
        curr.next = prev
        prev = curr
        curr = iterator
        iterator = iterator.next
        indx += 1


    curr.next = prev
    prev = curr
    return prev
