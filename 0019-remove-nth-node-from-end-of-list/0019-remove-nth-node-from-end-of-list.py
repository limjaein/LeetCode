# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return None

        size = 0
        
        cur = head
        while cur is not None:
            size += 1
            cur = cur.next
        
        cur = head
        move = size-n-1
        
        if move < 0:
            return head.next
        
        for i in range(move):
            cur = cur.next
                
        cur.next = cur.next.next
        
        return head