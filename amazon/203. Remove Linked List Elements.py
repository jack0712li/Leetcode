# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode(1)
        dummy.next = head
        pre = dummy
        cur = head

        while cur:
            next = cur.next
            if cur.val == val:
                while next and next.val == val:
                    next = next.next
                pre.next = next

            pre = cur
            cur = next

        return dummy.next