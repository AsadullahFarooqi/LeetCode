def mergeTwoLists(l1, l2):
    new_head = None
    if l1 == None:
        return l2
    elif l2 == None:
        return l2
    if l1.val <= l2.val:
        new_head = l1
        pt1 = l1.next
        pt2 = l2
    else:
        new_head = l2
        pt2 = l2.next
        pt1 = l1
    
    cp_head = new_head

    while pt1 != None and pt2 != None:
        if pt1.val <= pt2.val:
            new_head.next = pt1
            pt1 = pt1.next
        elif pt2.val < pt1.val:
            new_head.next = pt2
            pt2 = pt2.next

    if pt1 == None:
        new_head.next = pt2
    else:
        new_head.next = pt1
    return cp_head



def mergeTwoLists(l1, l2):
        new_head = None
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        if l1.val <= l2.val:
            new_head = l1
            pt1 = l1.next
            pt2 = l2
        else:
            new_head = l2
            pt2 = l2.next
            pt1 = l1
        
        cp_head = new_head

        while pt1 != None and pt2 != None:
            if pt1.val <= pt2.val:
                new_head.next = pt1
                pt1 = pt1.next
            elif pt2.val < pt1.val:
                new_head.next = pt2
                pt2 = pt2.next
            new_head = new_head.next
        if pt1 == None:
            new_head.next = pt2
        else:
            new_head.next = pt1
        return cp_head
