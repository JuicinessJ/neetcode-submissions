# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
        

# I am given the head of a linked list, and asked to reverse said list.
# With linked list, I cannot access each node as a list by indexing.
# Instead, I need to access each node by their pointer, going down the line...

# I am told I need to aim for O(n), meaning one loop, and O(1) for space, so no supporting list.
# This means, I cannot make a list, and append each element into said list.
# Instead, I need to 