# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #p l r n
        #p r l n 1. l -> n 연결 r -> l 연결 p -> r 연결
        
        cur = head
        prev = None
        
        while cur is not None:
            left = cur
            right = cur.next
            
            if left is not None and right is not None:
                
                # right connect
                left.next = right.next
                
                # left - right connect
                right.next = left
                
                # left connect
                if prev is not None:
                    prev.next = right
                else:
                    head = right
                    
            else:
                break
            
            prev = left
            cur = left.next
                
        return head