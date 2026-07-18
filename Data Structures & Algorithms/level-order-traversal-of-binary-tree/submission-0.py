# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []

        if not root:
            return []

        queue = [root]

        while queue:
            level = []

            for i in range(len(queue)):
                node = queue.pop(0)

                if node:
                    level.append(node.val)
                    
                    if node.left:
                        queue.append(node.left)

                    if node.right:
                        queue.append(node.right)

            ret.append(level)

        return ret

                

            

        

"""
I am given the root of a tree, and asked to return a list of this tree in level order traversal.
This means, I am expected to return a list of nodes at each level, from root, to the last leaf nodes.
For example, if I am given a tree, where root = [1,2,3,4,5,6,7].
The answer should be: [[1],[2,3],[4,5,6,7]]
Since if we visualize the tree, our root would be [1], our second level would be [2,3], and our lower level would be [4,5,6,7].

I am also told I should aim for O(n) for both time and space, this means no inner loops.

This means I should try a BFS or queue approach, first in first out.
As we traverse the list, we add the nodes into our return list.
As we access each level, we create a nested list, by recognizing the left and right nodes of the current root.
However, how would we create these list, and how would the recursive flow know its a new level and not the same level?

We could try creating temporary new list, as we recursively access the nodes, but only add those in the left and right nodes.
We could try using a hashset approach, assuming the tree is ordered, and we wont face duplicates.

But that still doesn't solve the level problem, how would be create a new level?

Idea:
When we recursively access each root level.
We have a left and right node

So during the first call, we have our root 1, which has a left 2, and right 3.
We add those into a list...

On our second call, we would call our new root 2, which has a left 4, and right 5.
On our third call, it would call our other new root within the queue 3, which has a left 6, and right 7.

However, how would the algo know that the second and third call should be the same level.
Assuming we might face an unbalanced tree, we could have 1 node per root...

To figure out how many nodes should be in each level, we could create a temporary stack.
This stack is intended to record size.

So when we first loop, we add the root into our stack.
After the first loop, we should remove this first entry, then add the next nodes entry.

So 1 goes in, which queues in 2 and 3.
One comes out, and 2 queues in 4, and 5, 3 queue
"""