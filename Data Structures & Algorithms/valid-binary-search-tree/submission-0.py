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

        

"""
I am given the root of a binary tree, and asked to determine if the tree is a valid binary search tree.
This is determined by the order of the tree, as in the leftmost node shall be the smallest and the rightmost be the largest.
Whereas the middle node shall be the middle, as in left <= mid <= right.
So essentially the left subtree's nodes should be less than the root, and right subtree larger than the root.
I am also told to aim for O(n) for both time and space.

For this, we could approach this with either a BFS or DFS approach.
If we do BFS, we would have to compare the left and right against the root.
If we do DFS, we would have to compare the left with root, and when we traverse up, we compare with right.

I think BFS may be easier since we wouldn't need to traverse back and forth.
Except, we could use DFS to discover depth, and when we traverse up one level, we compare that root with the left and right node.
Then we go upwards and start comparing.

So if we do DFS, we would first start with discovering depth, and when reached and traverse up, we compare with left and right.
By using recursion, we would essentially use a base case where the node is None or Null.

So hypothetically, if we are given a non-BST tree: [1,2,3,4,5,6,7].
We would traverse with 1->2->4, 4 would be the last since 4.left would be None.
Then we compare 3.left = 4, and 3.right = 5.
Since both left is larger than root, we'd return False.

I could try using a helper function that complements the verification.
While we compare the node with its left and right child.
We'd also compare the left and right node with a min and max val.
This min and max values are from their ancestors, providing a range.
Since we need to verify that there are no values within each subtree that are not compliant with a BST.
Where the left subtree must be less than the root, and the right subtree is greater than the root.

So when we traverse the left subtree (less than root), each current node will update max.
Since we want to ensure no values are greater than the previous roots.
And when we traverse the right subtree (greater than root), each current node will update min.
Since we want to ensure no values are less than the previous roots.

So at a high level, we recursively traverse the tree using a DFS approach (depth).
This will start with traversing the left subtree first.
Each left node must be less than the current root, and less than the previous root.
This is a given, however, when we compare the first right child at the lowest level.
We also need to ensure this value is less than the previous roots, and not just greater than the current root.
For example, if our previous root was 4 and current root is 2, or left is 1.
Our right could be any number greater than or equal to 3, and it would be correct.
However, we need to ensure this number is less than the previous root of 4.
So the value must be 3, this logic will be reversed for the right subtree.
Where the right subtree must be greater than the previous roots.
"""