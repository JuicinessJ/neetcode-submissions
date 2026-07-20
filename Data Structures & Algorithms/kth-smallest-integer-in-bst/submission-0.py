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
        

"""
I am given the root of a tree, and asked to return the kth smallest value within that tree.
Where this kth value represent a hypothetical index in a sorted list smallest to largest.
I am told I should aim for O(n) for both time and space.

The brute force method would be to traverse the tree and create a sorted list.
However, this may require O(n^2) approach, so we'd not be using this.

Another approach would be utilizing a DFS traversal, where we access the leftmost nodes as we traverse down.
Since this is a BST, we are ensured each left node will be the smallest compared to the root.
However, how would the algo know if the kth index value be inside the leftmost or perhaps a right node?

Apparently, the DFS we have been using aren't in-order, and they could be customized...

If we used a DFS/in-order traversal, where we traverse to the lowest level, checking the left node first.
Then the root node, then right, we would be accessing the tree in ascending order.
Since in a BST, the left < root < right.
So hypothetically, if we were given a tree = [2, 1, 3], where 1 is left, 2 is root, and 3 is right.
It would access left -> root -> right or 1 -> 2 -> 3.

So in this case, we'd use the DFS/in-order traversal, this gets us to the lowest number, or index 1.
We would create a counter that would have us keep traversing from left -> root -> right, until our counter == k.
"""