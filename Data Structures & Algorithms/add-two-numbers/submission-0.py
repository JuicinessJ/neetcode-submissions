# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carried_over = 0

        while l1 or l2 or carried_over:

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carried_over
            carried_over = total // 10

            curr.next = ListNode(total % 10)

            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next


"""
I am given two separate linked list, and asked to combine the values of nodes at each "index".
Meaning the first nodes of each linked list, I am asked to combine their value.
I am then asked to return the values of said combined nodes as a linked list.
Example: l1 = [1,2,3], l2 = [4,5,6] => [5,7,9].

To start, I am told to aim for O(m + n) for time, and O(1) for space.
This means no creating extra list elements...

To solve this, I am told to return as a linked list, so I will create a return LL.
I will also assume since the time complexity is O(m + n), this means size(l1) may not == size(l2).
This means with my loop, I will need to only loop if both l1 current, and l2 current are NOT None.

Issue: the values within may "overflow" resulting in numbers being carried over 
(ie. l1 = [9], l2 = [9] => [8, 1])

This means I will need to create a left over collection system or sum that stores any remaining sum.
This sum will need to be applied forwards...

Since our values are intended to represent the values between 0-9.
To find our "current node" value, we'll use sum % 10, this will give us the value to be added.
However, I will also need to create the collection or carried over value.
To find this value, we'll use sum // 10, this will return the floor value.
So 12 // 10 = 1, whereas 12 / 10 = 1.2, this extra / finds the floor value.

"""