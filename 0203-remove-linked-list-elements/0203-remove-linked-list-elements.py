# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        dummy = ListNode(next=head)
        prev = dummy
        curr = head

        while curr != None:
          if curr.val == val:
            nxt = curr.next
            prev.next = nxt
            curr = curr.next

          else:
            prev = prev.next
            curr = curr.next

        return dummy.next


        