class Solution:
    def reverseBetween(self, head: ListNode | None, left: int, right: int) -> ListNode | None:

        # Dummy node helps when left = 1
        dummy = ListNode(0)
        dummy.next = head

        # Move prev to the node just before left
        prev = dummy

        for _ in range(left - 1):
            prev = prev.next

        # Reverse the nodes between left and right
        current = prev.next

        for _ in range(right - left):
            next_node = current.next

            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next
