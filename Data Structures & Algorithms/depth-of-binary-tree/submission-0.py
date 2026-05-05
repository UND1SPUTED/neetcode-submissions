# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: #edge case: if tree is empty, dpeth is 0
            return 0

        #initialzie a quque with a root node
        queue = [root]

        depth = 0
        
        #loop unil the queue is empty
        while queue:

            #for each level count the number of nodes
            size = len(queue)

            #process all the nodes at the current level
            for i in range(size):
                node = queue.pop(0)

                # add left child to the queue if it exists
                if node.left:
                    queue.append(node.left)
                #add right child to the queue if it exists
                if node.right:
                    queue.append(node.right)
            #After processing one level, increment depth.
            depth += 1

        #return the depth as the result
        return depth
