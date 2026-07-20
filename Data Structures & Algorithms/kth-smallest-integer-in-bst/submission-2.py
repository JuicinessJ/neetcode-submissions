# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        counter = 0

        def kthIndex(root):
            
            nonlocal counter

            if not root:
                return None

            left = kthIndex(root.left)
            counter += 1

            if left != None:
                return left

            if counter == k:
                return root.val

            else:
                return kthIndex(root.right)
            
            
        return kthIndex(root)