# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def traverse(node):

            if not node:
                return 0

            return 1 + max(traverse(node.left), traverse(node.right))

        return traverse(root)
        

# Input: root of binary tree
# Output: number representing max depth of either branch

# We can find the deepest branch by traversing our tree and return a + 1 if we can continue traversing, else at None we return 0.