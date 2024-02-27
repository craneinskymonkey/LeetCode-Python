class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        tail_of_left = dummy

        for i in range(m - 1):
            tail_of_left = tail_of_left.next

        tail_of_reverse_list = tail_of_left.next
        prev, current = None, tail_of_left.next

        for i in range(m, n + 1):
            next, current.next = current.next, prev
            prev, current = current, next

        tail_of_reverse_list.next = current
        tail_of_left.next = prev

        return dummy.next
