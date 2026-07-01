# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        while fast != None and fast.next != None:

            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True

        return False
        
        

# I am given a linked list, and asked to find out if this list is a cycle.
# Meaning it repeats somewhere...
# I am asked to keep it within O(n) for time, and O(1) for space.
# This means I cannot use any supporting list, including hashmaps or sets, and alloted one loop.

# The easiest method, would be iterating through the list, and appending each node into a set.
# If a duplicate is found, we return true...

# However, since I cannot use a hashmap or set.
# The other method would be a fast and slow pointer approach.
# Where we have two separate pointers, accessing the same linked list.
# And if they ever intersect, then we have a cycle.