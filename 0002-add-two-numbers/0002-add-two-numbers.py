# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list1 = []
        list2 = []

        while l1 != None:
            list1.append(str(l1.val))
            l1 = l1.next

        while l2 != None:
            list2.append(str(l2.val))
            l2 = l2.next

        i1 = int(''.join(list1[::-1]))
        i2 = int(''.join(list2[::-1]))

        sum_str = str(i1 + i2)
        result = ListNode(sum_str[0])

        for (i, num) in enumerate(sum_str):
            if i != 0:
                result = ListNode(num, result)
                
        return result