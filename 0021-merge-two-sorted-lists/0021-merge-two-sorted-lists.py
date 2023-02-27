# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = cur = ListNode(-1)
        
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            else:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            
            cur = cur.next
        
        while list1 is not None:
            cur.next = ListNode(list1.val)
            cur = cur.next
            list1 = list1.next
        
        while list2 is not None:
            cur.next = ListNode(list2.val)
            cur = cur.next
            list2 = list2.next
        
        return head.next
                
            
        