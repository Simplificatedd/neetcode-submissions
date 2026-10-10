# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None or head.next is None:
            return

        slow_pointer = head
        fast_pointer = head

        while (fast_pointer != None) and (fast_pointer.next != None):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        previous = None
        current = slow_pointer.next
        slow_pointer.next = None

        while current != None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        first = head
        second = previous
        while second != None:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2