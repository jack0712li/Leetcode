# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if not head:
            return True
        recorder = []

        cur = head

        while cur:
            recorder.append(cur.val)
            cur = cur.next

        left = 0
        right = len(recorder)-1

        while left < right:
            if recorder[left] != recorder[right]:
                return False
            left += 1
            right -=1

        return True 