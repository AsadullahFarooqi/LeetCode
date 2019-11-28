# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists or not all(lists):
            return None

        head = ListNode(float("inf"))
        # finding a head
        temp_head = head
        
        while temp_head != None:
            min_ = 0
            for lists[i] in lists:
                if lists[i].val <= lists[min_].val:
                    min_ = i

            temp_head.next = lists[min_]
            temp_head = temp_head.next

            if lists[min_].next != None:
                lists[min_].val = lists[min_].next.val
                lists[min_].next = lists[min_].next.next
            else:
                lists.remove(lists[min_])

        e = head
        while e != None:
            print(e.val, ends=" -> ")
            e = e.next
        
