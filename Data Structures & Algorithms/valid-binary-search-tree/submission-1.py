# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # empty tree = valid BST
        if not root:
            return True

        min_val, max_val = float('-inf'), float('inf')

        def validate(node, min_val, max_val):

            if not node:
                return True

            if min_val < node.val and node.val < max_val:

                return (validate(node.left, min_val, node.val) and validate(node.right, node.val, max_val))

            else:
                return False

        return validate(root, min_val, max_val)