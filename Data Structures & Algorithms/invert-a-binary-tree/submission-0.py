# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left, root.right = root.right, root.left

        return root
        
        


"""
I am given the root of a tree, and asked to return the inverse.
Meaning, I flip the left with the right literally.
The root will be left alone, but as we traverse down the tree, we'll need to flip the left with right of said root.

I am told I need to aim for O(n) for both space and time.
This means no inner loop, and I can create supporting list.
This list could be a stack, queue, hashs, or just list...

Since we are looking to invert the tree, I need to figure out how we can utilize a supporting list.
If we treated this problem as a DFS (stack), nodes will enter like: [1,2,4,5,3,6,7]
If we treated this problem as a BFS (queue), nodes will enter like: [1,2,3,4,5,6,7]

If we used the DFS approach, to output the nodes in inverse order, I would hug the right side.
But how do we know when to stop hugging and start building the level...
Because we could go [1,2,4] but after 4, 5 should be on the same level, but it doesn't know it needs to build, instead it continues the right.
So...

If we used the BFS approach, to output the nodes in inverse order, I would need to output level by level.
But we'd just need to start seeding right first, then left.
After the first level is built, we go to root.right
"""
