# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        return depth 






"""
I am the root of a tree, and asked to find the maximum depth within this tree.
I am told I should aim for O(n) for time, and O(n) for space
This means no inner loops, and I may create additional list for support if needed...

To find the depth of a tree, I should realistically be using a DFS approach, since we are looking for "depth".
We should only increment when we are accessing a leaf node, however, we shouldn't increment when we are accessing each left node.
Since there may be a left and right leaf node...

By utilizing a DFS approach, we will theoretically be recursively or iteratively calling the left leaf node, until there is no more.
We should increment a depth counter each time the left node is called.
We might need to do the same thing for the right, if our right branch is deeper than left
However, as mentioned, we shouldn't increment each time a leaf node is called, only when reaching a new depth...

We should only update the counter if we are going deeper, and if the depth of left or right is deeper than one another.
However, how would we know if the counter should be updated?
Especially since we may not know if a new node is a new depth.

We are guaranteed that if we are traversing the left node from root, it is reaching a new level, so we can update depth.
However, what happens if we have expended all left, and climb up one, to call the right.
We shouldn't update if we climb up one, only if we are going down one.
But what if that level has already been explored.
How would the algo know if the level have been explored...

What if we used a hashset to check if the value have already been explored.
But again how would we know if this value is a new depth...
"""