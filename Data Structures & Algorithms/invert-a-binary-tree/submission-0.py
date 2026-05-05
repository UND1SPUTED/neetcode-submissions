# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: #edge case: if root is empty
            return None

        stack = [root] #initialize the root code 

        while stack:
            node = stack.pop() #get current node

            #swap left and right children
            node.left, node.right = node.right, node.left

            #add children to stack if they exist
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return root #Return to the new root