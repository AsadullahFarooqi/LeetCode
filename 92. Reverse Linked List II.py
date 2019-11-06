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


def reverseBetween(head, m, n):
        if head == None or head.next == None:
            return head
        elif head.next.next == None:
            h = head
            head = head.next
            head.next = h
            h.next = None
            return head
        elif m == n:
            return head

            
        curr = head
        if m > 1:
            indx = 1
            while indx < m-1:
                curr = curr.next
                indx += 1

            a = curr
            prev = a
            curr = curr.next
        else:
            indx = 0
            a = None
            prev = None
            curr = head
        b = curr
        indx += 1
        while indx <= n:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            indx += 1

        if a != None:
            a.next = prev
            b.next = temp

        return head

