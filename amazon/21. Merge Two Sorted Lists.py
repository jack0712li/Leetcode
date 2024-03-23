# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(-101)
        cur = dummy
        cur1 = list1
        cur2= list2

        while cur1 and cur2:
            if cur1.val >= cur2.val:
                cur.next = cur2
                cur2 =cur2.next

            else:
                cur.next = cur1
                cur1 = cur1.next
            cur = cur.next

        if not cur1:
            cur.next = cur2
        else:
            cur.next = cur1

        return dummy.next

                
        