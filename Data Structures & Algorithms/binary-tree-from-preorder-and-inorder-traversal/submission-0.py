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

        
            



        

"""
I am given two separate list, both of which represents the same tree in structure and values.
Except they're ordered differently, due to their traversal order, pre-order, and in-order.
I am asked to rebuild this tree from both list and their unique orders and return its root.

Pre-Order: Root -> Left -> Right
In-Order: Left -> Root -> Right

Since both list are created from different traversal order, I may not be able to use the same function to rebuild the same tree.
This means, If I decide to use recursion and create helper functions, I may need to make two separate helper functions.
One for the in-order traversal, and the other for the pre-order traversal.

Starting with the pre-order traversal, since pre-order is root -> left -> right.
The value at index of 0 should be the root, index @ 1 would be left.
However with pre-order, as it visits the left node, it updates as root, so it'll indefintely visit the left nodes first.
Before visiting a right node, which will happen when it encounters a None/Null.
So when index @ 0 = root, and index @ 1 = left, index @ 2, could be another left node.

With in-order traversal, since in-order is left -> root -> right.
The value @ index of 0 should be left, however, with in-order, it doesn't read in the first left node from root.
It traverses down the tree indefintely until it encounters as None/Null, before it considers that value, or read that root.
So when index @ 0 could equal a left node at any level.

Since this tree isn't a valid BST, theres no guarantee where the values should fall in-line.
If I was to create a model, we'd start with pre-order, this can rule our the first two indices.
We know with pre-order the first two indices would be root then left.
However, the third index could be another left, or the first right.

If I could somehow combine this logic with the in-order, we'd could remove the first two indices...
or perhaps the first two values from pre-order in in-order, using a hashset...
since this would inform the model, that these values have been used or seen.

If the first two indices of in-order also share the same values in pre-order, then we could assume the nodes location.

For example with the given example of: preorder = [1,2,3,4], inorder = [2,1,3,4]

The first two indices of pre-order are roughly equal to in-order, thought at different location.
If we were able to have the model understand that from pre-order that 1 is root...
we could somehow tell that the 1 @ index of 1 is root, this would mean, we are now traversing the right subtree...

However, since we know that the first index of preorder will always be the root.
If we consider using a divide and conquer method, of spliting the inorder.
We could come up with a solution.

For example, the first value within a preorder is the root.
The second would be the left node, which is another root of the left subtree.

Example:
preorder = [1, 2, 4, 7, 3, 5, 6]
inorder  = [4, 7, 2, 1, 5, 3, 6]

So the solution is we first find the middle (root) of each subset we are given from splitting in-order.
First split is 1, since preorder first index is root.
We split inorder at value == 1, which is index 3, so our subset would be:
first split left = [4,7,2]
first split right = [5,3,6]

The second split should be at index of 1 in preorder or value 2.
This value is the first left root, from the subsets of the first split in left and right.
We find that 2 is in index of 2 of inorder, so if we split there.
second split left = [4,7]
second split right = [5,3,6]
Since 2 exist in the left and not the right.

The third split should be at index of 2 in preorder, so value 4.
This value is the next left root, from the subsets of the previous splits of left and right.
We find that value 4 is in index of 0 of inorder, so if we split there.
third split left = [7]
second split right = [5,3,6]
Since 4 exist in the left and not the right.
But since 7 is after 4, and not before as of value 2 from the second split.
We know this value would be a right node.
Since inorder is left -> root -> right.
Any value on the right of the split is in the right, and any in the left of the split is in the left.

Find root then split inorder at value index.
Any value on the left of split is left subset, and value on the right of split is right subset.
Keep splitting until we reach length of 0.

"""