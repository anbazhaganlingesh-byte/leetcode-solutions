# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sl=head
        fst=head
        while fst is not None and fst.next is not None:
            sl=sl.next
            fst=fst.next.next
            if sl==fst:
                return True
        return False