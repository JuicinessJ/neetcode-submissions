# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if len(inorder) == 0:
            return None

        if len(inorder) == 1:
            return TreeNode(inorder[0])

        split = preorder[0]
        left = []
        right = []

        for i in range(len(inorder)):
            if inorder[i] == split:
                left = inorder[0:i]
                right = inorder[i + 1:]

        root = TreeNode(split)

        root.left = self.buildTree(preorder[1:len(left) + 1], left)
        root.right = self.buildTree(preorder[len(left) + 1:], right)

        return root