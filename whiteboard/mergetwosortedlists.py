"""Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        # solved using iteration approach.
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # set head(h) and tail(t) to detail last node in the list.
        h = t = ListNode(0)
        
        # while loop  appends l1 or l2 to tail, updates the tail of l1 and l2 accordingly.
        while l1 and l2:
            if l1.val <= l2.val:
                t.next = l1
                l1 = l1.next
            else:
                t.next = l2
                l2 = l2.next
            t = t.next
        t.next = l1 or l2
        return h.next

"""Runtime: 28 ms, faster than 68.88% of Python online submissions for Merge Two Sorted Lists.
Memory Usage: 12.8 MB, less than 35.77% of Python online submissions for Merge Two Sorted Lists."""
