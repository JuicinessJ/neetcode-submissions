# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:

            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

     


# I am given two sorted linked list, and asked to merge into one sorted linked list and return the result.
# I am told I should aim for O(n + m) for time, and O(1) for space.
# This means no extra list for support, beside the linked list itself.

# Since I am return a sorted linked list, I will need to iterate through each list when the condition is true.
# This condition should be if the value is used.
# The value that will be used is if is less than the counterpart.
# This means I will iterate through the linked list that has the lesser value.

