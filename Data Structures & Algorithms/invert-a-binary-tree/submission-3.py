# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def traverse(node):
            if not node:
                return None

            traverse(node.left)
            traverse(node.right)

            copy = node.left
            node.left = node.right
            node.right = copy

        traverse(root)
    
        return root

# Input: tree
# Output: same tree inverted, where left branch is now right, etc.

# To begin, with any tree, our first goal is to finish traversing the tree, before we begin inverting branches.
# From our root node, we'll traverse down until we reach the last node before its leaf.
# Here, we'll invert the tree, by setting node.left = node.right, and node.right = node.left.
# This will require a temporary copy of either node when setting.