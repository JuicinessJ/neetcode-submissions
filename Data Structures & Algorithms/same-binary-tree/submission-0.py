# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        
        if not p or not q or p.val != q.val:
            return False


        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)





        

"""
I am given the roots of two separate trees, and asked to check if they're identical.
For them to be identical, they'll need to have the same structure and nodes with the same values.
I am told to aim for O(n) for time and space, this means no inner loops, and I have create supporting list if needed.

Since we are attempting to test if the trees provided are identical, we could use either approaches.
However, I think BFS may be the best approach here, since we are looking to test structure and not depth.

I could try and compare their outputs in list format, but this wouldn't test for structure only order
I could try iterating through the trees together and check if their values continue to match.
Since our function have 3 params, with two being roots, this solves how I would recurisvely call them.

In reality, I don't think either approach matters, since our function takes two tree values as params.
With this info, we just need to have a test case inside that checks if the values provided == one another.
If they do, we continue through the tree.
If they don't, we stop and return False, else return True.
"""