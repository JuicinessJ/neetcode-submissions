"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        map = {None: None}
        curr = head

        while curr:
            copy = Node(curr.val)
            map[curr] = copy
            curr = curr.next

        curr = head

        while curr:
            copy = map[curr]
            copy.next = map[curr.next]
            copy.random = map[curr.random]
            curr = curr.next

        return map[head]
        





        

"""
I am given the head of a linked list, and asked to return a copy similar to our linked list.
However, I am not returning the input as output literally...

Instead, I need to access each node within the linked list, and make a copy while preserving their pointers.
However, this linked list, doesn't have just one pointer, instead it has two.
With the second pointer having the options of pointing at a different node within the same linked list.
Or at a None/null value...
This means, our second pointer could point with the first pointer, somewhere else, or at null...

I am also told I should aim for O(n) for space and time.
This means I am expected to make no inner loops, and am allowed to use list.
With list, I could make a simple list, or hashmaps or sets.

This problem doesn't specify frequency or existence, so hashmap and/or set may not be necessary.
However, I am alerted that "None of the pointers in the new list should point to nodes in the original list".
This means new nodes don't touch old nodes.
So hashset may become used here...
But this isn't asking about existence, merely mentioning that we should make sure they aren't pointing to old nodes...

Had this been singly linked, I could've just went through the linked list, and copy and paste.
However, since there is additional pointer, I need to figure out how we can point to a node that doesn't exist yet.
I could try using the dummy node method from previous problems, but how would we know when to replace/update the info...

Does the extra null value only exist for the head node, or can it be expected in-between...
If it exist on the head, we just use the dummy and point it as tails, similarly to a earlier problem.
If it exist in-between, then we have a problem...

However, disregarding that for now, what about the pointers with values beside null.
What if the node haven't been created yet.
How do we point at a empty node...

Can I just point at dummy and update later, but how do we replace/update the value...
"""